#!/usr/bin/env python3
"""Check that the installed Skill contains its required runtime files.

This is a structural check, not a checksum or dependency check. It does not
modify the installation and uses only the Python standard library.
"""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_FILES = (
    "SKILL.md",
    "LICENSE",
    "references/win-local.md",
    "scripts/attribution_guard.py",
    "scripts/bootstrap_env.py",
    "scripts/project_manager.py",
    "scripts/svg_quality_checker.py",
    "scripts/svg_to_pptx.py",
    "templates/design_spec_reference.md",
    "templates/spec_lock_reference.md",
    "templates/schemas/design_spec.schema.json",
    "templates/schemas/spec_lock.schema.json",
    "templates/scaffolds/design_spec.md",
    "templates/scaffolds/spec_lock.md",
    "workflows/routing.md",
    "workflows/generate-pptx.md",
    "workflows/edit-native-pptx.md",
    "workflows/create-template.md",
    "workflows/profiles/quick-generate.md",
    "workflows/profiles/beautify-pptx.md",
    "workflows/profiles/image-to-pptx.md",
)


def missing_files(root: Path) -> list[str]:
    """Return required relative paths absent from an installed Skill root."""
    return [relative for relative in REQUIRED_FILES if not (root / relative).is_file()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1],
                        help="installed Skill directory (default: containing package)")
    args = parser.parse_args(argv)
    missing = missing_files(args.skill_dir)
    if missing:
        print("Incomplete Skill package; missing required files:")
        for relative in missing:
            print(f"  {relative}")
        print("Reinstall a complete package. Installing Python dependencies cannot restore these files.")
        return 2
    print(f"Skill package structure OK ({len(REQUIRED_FILES)} required files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
