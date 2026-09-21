#!/usr/bin/env python3
"""win-ppt - Export compatibility wrapper using the current PPTX exporter.

Usage:
    python3 scripts/run_svg_to_pptx.py <project_path> [export_options]

Dependencies:
    Current exporter dependencies; preserved Windows CPython 3.13 bundle is a
    Windows-only fallback and never shadows macOS/Linux native packages.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
if sys.platform == 'win32' and sys.version_info[:2] == (3, 13):
    try:
        import PIL.Image
        import lxml.etree
        import pptx
    except ImportError:
        sys.path.insert(0, str(SCRIPTS_DIR.parent / 'lib'))
sys.path.insert(0, str(SCRIPTS_DIR))
spec = importlib.util.spec_from_file_location('win_export_entry', SCRIPTS_DIR / 'svg_to_pptx.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

if __name__ == '__main__':
    raise SystemExit(module.main())
