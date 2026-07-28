#!/usr/bin/env python3
"""Remove markdown heading and following blank line from all .md files.

Looks for files where:
- Line 1 starts with '# ' (markdown heading)
- Line 2 is blank (empty or whitespace-only)

When both conditions are met, removes both lines.
"""

import os
import glob


def process_file(filepath: str) -> bool:
    """Process a single markdown file. Returns True if modified."""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Need at least 2 lines
    if len(lines) < 2:
        return False

    # Check if line 1 is a markdown heading and line 2 is blank
    if not lines[0].startswith("# "):
        return False

    if lines[1].strip() != "":
        return False

    # Remove the first two lines (heading + blank line)
    new_lines = lines[2:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    return True


def main():
    # Find all .md files recursively
    md_files = glob.glob("**/*.md", recursive=True)

    modified_count = 0
    skipped_count = 0

    for filepath in sorted(md_files):
        # Skip the script itself if it ends up as .md (it won't, but be safe)
        if filepath == "remove_headings.py":
            continue

        if process_file(filepath):
            print(f"Modified: {filepath}")
            modified_count += 1
        else:
            skipped_count += 1

    print(f"\nDone. Modified: {modified_count}, Skipped (no matching pattern): {skipped_count}")


if __name__ == "__main__":
    main()