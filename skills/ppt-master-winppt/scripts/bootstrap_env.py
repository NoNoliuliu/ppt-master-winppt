#!/usr/bin/env python3
"""Check/install dependencies for one capability in the selected venv.
Exit: 0 selected profile ready, 1 check-only missing, 2 selected profile failure.
A preview-profile failure does not imply PPT generation is unavailable.
"""
import argparse
import contextlib
import io
from pathlib import Path
import json
import subprocess
import sys

from check_skill_package import missing_files

CORE = [
    ("PyYAML>=6.0", "yaml"), ("python-pptx>=0.6.21", "pptx"),
    ("lxml", "lxml.etree"), ("Pillow>=9.0.0", "PIL.Image"),
    ("XlsxWriter>=3.0.0", "xlsxwriter"),
]
PREVIEW = [("flask>=3.0.0", "flask")]
OPTIONAL = [
    ("skia-pathops", "pathops"), ("uharfbuzz", "uharfbuzz"),
    ("edge-tts", "edge_tts"), ("PyMuPDF", "fitz"),
    ("mammoth", "mammoth"), ("openpyxl", "openpyxl"),
    ("requests", "requests"), ("beautifulsoup4", "bs4"),
    ("curl_cffi", "curl_cffi"), ("markdownify", "markdownify"),
    ("ebooklib", "ebooklib"), ("nbconvert", "nbconvert"),
]
# Each pass runs in a fresh interpreter: failed/partial imports cannot pollute
# post-install verification. Import the native modules actually used at runtime.
PROBE = r"""
import importlib, importlib.metadata, json, re, sys
rows = []
for requirement, module in json.loads(sys.argv[1]):
    package, _, minimum = requirement.partition('>=')
    try:
        importlib.import_module(module)
        if minimum:
            version = importlib.metadata.version(package)
            numeric = lambda value: tuple(int(x) for x in re.match(r'^\d+(?:\.\d+)*', value).group().split('.'))
            if numeric(version) < numeric(minimum):
                raise RuntimeError('installed version below required minimum')
        rows.append({'requirement': requirement, 'module': module, 'ok': True})
    except Exception as exc:
        rows.append({'requirement': requirement, 'module': module, 'ok': False, 'error': type(exc).__name__})
print('BOOTSTRAP_RESULT=' + json.dumps(rows))
"""


def probe(packages):
    result = subprocess.run([sys.executable, '-c', PROBE, json.dumps(packages)],
                            capture_output=True, text=True, timeout=120)
    if result.returncode:
        raise RuntimeError('dependency probe process failed')
    for line in reversed(result.stdout.splitlines()):
        if line.startswith('BOOTSTRAP_RESULT='):
            return json.loads(line.split('=', 1)[1])
    raise RuntimeError('dependency probe returned no result')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true', help='never install')
    parser.add_argument('--profile', choices=['ppt', 'preview'], default='ppt',
                        help='check/install only dependencies of this capability')
    parser.add_argument('--report', help='write diagnostic output as UTF-8 without shell redirection')
    args = parser.parse_args(argv)
    if args.report:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = run(args)
        try:
            Path(args.report).write_text(output.getvalue(), encoding='utf-8')
        except OSError:
            print('[bootstrap] cannot write report')
            return 2
        return code
    return run(args)


def component_status(root):
    return {name: (root / relative).is_file() for name, relative in {
        'ppt_export': 'scripts/svg_to_pptx.py',
        'quality_checker': 'scripts/svg_quality_checker.py',
        'confirmation_ui': 'scripts/confirm_ui/server.py',
        'live_preview': 'scripts/svg_editor/server.py',
    }.items()}


def run(args):
    skill_root = Path(__file__).resolve().parents[1]
    missing = missing_files(skill_root)
    if missing:
        print('Incomplete Skill package; missing required files:')
        for relative in missing:
            print(' ', relative)
        print('Reinstall a complete package. Pip cannot restore Skill files.')
        return 2
    components = component_status(skill_root)
    print('[bootstrap] components:', json.dumps(components))
    if not components['ppt_export'] or not components['quality_checker']:
        print('Incomplete Skill package: restore from the published package; pip cannot install missing Skill scripts.')
        return 2
    if args.profile == 'preview' and not components['live_preview']:
        print('Preview component absent: use chat and continue PPT; restore the complete Skill for preview. Pip cannot repair it.')
        return 2
    if not components['confirmation_ui']:
        print('Confirmation UI absent: use chat confirmation; PPT remains available.')
    required = CORE if args.profile == 'ppt' else PREVIEW
    extras = PREVIEW + OPTIONAL if args.profile == 'ppt' else []
    print('[bootstrap] interpreter:', sys.executable)
    print('[bootstrap] Python:', sys.version.split()[0])
    if sys.version_info < (3, 10):
        print('Python 3.10+ required; select a compatible interpreter. No installation attempted.')
        return 2
    try:
        rows = probe(required + extras)
        core = rows[:len(required)]
        for row in rows:
            print(('core' if row in core else 'optional'), row['requirement'],
                  'ok' if row['ok'] else 'unavailable (' + row['error'] + ')')
        missing = [r['requirement'] for r in core if not r['ok']]
        print('Optional dependencies are route-specific; absence does not block core readiness.')
        if not missing:
            print('[bootstrap]', args.profile, 'dependencies ready')
            return 0
        if args.check_only:
            print('Required:', ', '.join(missing))
            return 1
        if sys.prefix == sys.base_prefix:
            print('Refusing to install into system/global Python. Create or select a writable venv, then rerun with its Python.')
            return 2
        cmd = [sys.executable, '-m', 'pip', 'install', '--disable-pip-version-check',
               '--no-input', '--retries', '1', '--timeout', '30', *missing]
        # Do not echo pip output: corporate index/proxy URLs may contain credentials.
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        if result.returncode:
            print('pip failed (code %s). Check venv permissions/pip availability and your approved corporate index or proxy configuration. Do not disable TLS or use --break-system-packages.' % result.returncode)
            return 2
        remaining = [r['requirement'] for r in probe(required) if not r['ok']]
        if remaining:
            print('Still unavailable:', ', '.join(remaining))
            return 2
        print('[bootstrap]', args.profile, 'dependencies ready after installation')
        return 0
    except (OSError, RuntimeError, ValueError, subprocess.TimeoutExpired) as exc:
        print('[bootstrap] check/install failed:', type(exc).__name__)
        return 2


if __name__ == '__main__':
    sys.exit(main())
