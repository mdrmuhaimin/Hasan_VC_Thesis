#!/usr/bin/env python3
"""
Compile 'Interview Notes' from multiple files into a single Markdown.

This script scans a directory for Markdown/text files, extracts:
  - H2 name header matching: "## 28. Name: <Person>" or "## Name: <Person>"
  - H3 notes header matching: "### Interview Notes:" (colon optional, case-insensitive)

Then it writes a combined Markdown in the format:

## Name: <Person>
### Interview Notes:
<notes...>

Usage:
  python compile_interview_notes.py --input /path/to/folder --output compiled_interview_notes.md

Options:
  --ext to add/override glob patterns (default: *.md *.markdown *.txt)
"""

import argparse
import glob
import os
import re
from typing import Optional, List, Dict

# Regex for the H2 name header, e.g.:
#   ## 28. Name: Tahmeed Sharif
#   ## Name: Tahmeed Sharif
H2_NAME_RE = re.compile(r'^##\s*(?:(\d+)\.\s*)?Name:\s*(.+?)\s*$', re.IGNORECASE)

# Regex for the '### Interview Notes' header (colon optional)
H3_NOTES_RE = re.compile(r'^###\s*Interview\s*Notes:?[\s]*$', re.IGNORECASE)

# Regex for any Markdown header line (to detect end of section)
ANY_HEADER_RE = re.compile(r'^\s*#{1,6}\s+\S')

def parse_file(path: str) -> Optional[Dict]:
    """Parse a single file, returning a dict with 'order', 'name', 'notes', 'file'; or None if not found."""
    try:
        with open(path, 'r', encoding='utf-8-sig') as f:
            lines = f.read().splitlines()
    except UnicodeDecodeError:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.read().splitlines()

    order_num = None
    name = None

    # Find the H2 name header
    for line in lines:
        m = H2_NAME_RE.match(line)
        if m:
            if m.group(1):
                try:
                    order_num = int(m.group(1))
                except ValueError:
                    order_num = None
            name = m.group(2).strip()
            break

    if not name:
        # If no H2 name header, skip this file
        return None

    # Find start of "### Interview Notes"
    start_idx = None
    for i, line in enumerate(lines):
        if H3_NOTES_RE.match(line):
            start_idx = i + 1  # content starts after this line
            break

    if start_idx is None:
        # No Interview Notes section
        return None

    # Capture until the next header or EOF
    collected: List[str] = []
    for j in range(start_idx, len(lines)):
        if ANY_HEADER_RE.match(lines[j]):
            break
        collected.append(lines[j])

    # Trim trailing blank lines
    while collected and collected[-1].strip() == '':
        collected.pop()

    notes = '\n'.join(collected).rstrip()

    return {
        'order': order_num,
        'name': name,
        'notes': notes,
        'file': os.path.basename(path),
    }

def main():
    ap = argparse.ArgumentParser(description="Compile Interview Notes from multiple files.")
    ap.add_argument('--input', '-i', default='.', help='Directory containing source files (default: current dir)')
    ap.add_argument('--output', '-o', default='compiled_interview_notes.md', help='Output Markdown file path (default: compiled_interview_notes.md)')
    ap.add_argument('--ext', nargs='*', default=['*.md', '*.markdown', '*.txt'],
                    help='File glob patterns (default: *.md *.markdown *.txt)')
    ap.add_argument('--verbose', action='store_true', help='Print skipped files and progress')
    args = ap.parse_args()

    src_dir = os.path.abspath(os.path.expanduser(args.input))
    if not os.path.isdir(src_dir):
        raise SystemExit(f"[error] Input directory not found: {src_dir}")

    # Collect files
    patterns = [os.path.join(src_dir, pat) for pat in args.ext]
    files: List[str] = []
    for p in patterns:
        files.extend(glob.glob(p))

    files = sorted(set(files))
    if not files:
        raise SystemExit("[info] No files found. Check --input and --ext patterns.")

    parsed: List[Dict] = []
    for fp in files:
        result = parse_file(fp)
        if result:
            parsed.append(result)
            if args.verbose:
                print(f"[ok] Parsed: {result['file']} -> {result['name']}")
        else:
            if args.verbose:
                print(f"[skip] No matching headers in: {os.path.basename(fp)}")

    if not parsed:
        raise SystemExit("[info] No valid 'Name' + 'Interview Notes' sections found.")

    # Sort: numeric order if present, then by name
    def sort_key(x: Dict):
        return (x['order'] if x['order'] is not None else 10**9, x['name'].lower())

    parsed.sort(key=sort_key)

    # Build output
    out_lines: List[str] = []
    for item in parsed:
        out_lines.append(f"## Name: {item['name']}\n")
        out_lines.append("### Interview Notes:\n")
        if item['notes'].strip():
            out_lines.append(item['notes'].rstrip() + "\n")
        else:
            out_lines.append("_No notes found in this file._\n")
        out_lines.append("\n")

    # Write output safely (handles cases like -o compiled.md)
    output_path = os.path.abspath(os.path.expanduser(args.output))
    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines).rstrip() + '\n')

    print(f"[done] Compiled {len(parsed)} entries into: {output_path}")

if __name__ == '__main__':
    main()
