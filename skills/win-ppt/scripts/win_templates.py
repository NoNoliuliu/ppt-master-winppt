#!/usr/bin/env python3
"""win-ppt - Local Weining template compatibility commands.

Usage:
    Use project_manager.py list-templates or import-template <project> <name>.

Dependencies:
    Standard library; upstream apply_template.py for installation.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent


def list_templates() -> None:
    """List the preserved local template choices."""
    options = json.loads((SKILL_DIR / 'templates/win-layouts-index.json').read_text(encoding='utf-8'))
    for name, info in options.items():
        print(f"{name}: {info['summary']}")


def import_template(project_path: str, template_name: str) -> int:
    """Install an explicitly selected local template through the current installer."""
    options = json.loads((SKILL_DIR / 'templates/win-layouts-index.json').read_text(encoding='utf-8'))
    if template_name not in options:
        raise ValueError(f'Unknown local template: {template_name}')
    root = SKILL_DIR / 'templates/decks' / template_name
    return subprocess.run([
        sys.executable, str(SKILL_DIR / 'scripts/apply_template.py'),
        str(Path(project_path).expanduser().resolve()), '--root', str(root),
    ], check=False).returncode
