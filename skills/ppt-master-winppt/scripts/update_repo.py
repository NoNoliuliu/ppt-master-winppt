#!/usr/bin/env python3
"""ppt-master-winppt - Managed update notice. Use the Obsidian Skill registry."""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="ppt-master-winppt updates are merged in an isolated candidate and published through the Obsidian Skill registry.")
    parser.add_argument("--skip-pip", action="store_true")
    parser.parse_args()
    print("Use obsidian-skill-registry: skill-context, skill-drift-check, isolated upstream merge, audit, user approval, skill-publish, skill-sync. Direct deployment updates are disabled.", file=sys.stderr)
    return 2

if __name__ == "__main__":
    raise SystemExit(main())
