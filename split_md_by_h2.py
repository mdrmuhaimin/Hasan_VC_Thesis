#!/usr/bin/env python3
"""
Split a large Markdown file into multiple files by second-level headings.

Rules:
- Each section starts at a line that begins with "## " (a second-level heading)
  that is NOT inside a fenced code block.
- A section includes that "## " line and all following lines up to (but not
  including) the next "## " (outside code), or end of file.
- Third-level (###) and deeper headings remain within their parent section.
- The top-level "# Interview notes" header is ignored for splitting.
- Filenames are derived from the second-level heading text and de-duplicated.

Usage:
    python split_md_by_h2.py input.md output_dir

Options:
    --prefix "Interview_"         Add prefix to output filenames
    --include-top                 Prepend the top-level header (if present) to each output file
"""

import argparse
import os
import re
import sys
from pathlib import Path

H2_PATTERN = re.compile(r'^(##)\s+(.*)$')        # second-level heading
H1_PATTERN = re.compile(r'^(#)\s+(.*)$')         # top-level heading
FENCE_PATTERN = re.compile(r'^(```|~~~)')        # start/end of fenced code block
TRAILING_HASHES = re.compile(r'\s+#+\s*$')       # strip trailing ### in ATX headers

def sanitize_filename(text: str, max_len: int = 120) -> str:
    """
    Convert heading text to a safe filename.
    Keeps letters, numbers, spaces, dashes, underscores, and dots.
    Collapses whitespace to single underscores. Trims length.
    """
    # Remove trailing ' #' in headers like "## Title ###"
    text = TRAILING_HASHES.sub('', text).strip()

    # Replace path-separators and forbidden chars on common OSes
    text = re.sub(r'[\\/:*?"<>|]+', ' ', text)

    # Keep a conservative set of characters
    text = re.sub(r'[^A-Za-z0-9._ -]+', '', text)

    # Collapse whitespace to underscore
    text = re.sub(r'\s+', '_', text).strip('_')

    if not text:
        text = "section"

    return text[:max_len]

def open_new_section(out_dir: Path, base_name: str, used_names: dict, prefix: str = ""):
    """
    Open a new file for a section, de-duplicating filename if needed.
    Returns (file_handle, filepath).
    """
    base = sanitize_filename(base_name)
    candidate = f"{prefix}{base}.md"
    idx = 2
    while candidate.lower() in used_names:
        candidate = f"{prefix}{base}_{idx}.md"
        idx += 1
    used_names[candidate.lower()] = True
    fp = (out_dir / candidate).open('w', encoding='utf-8', newline='\n')
    return fp, out_dir / candidate

def split_markdown_by_h2(input_path: Path, output_dir: Path, prefix: str = "", include_top: bool = False):
    output_dir.mkdir(parents=True, exist_ok=True)

    in_code_fence = False
    fence_delim = None
    current_file = None
    current_path = None
    used_names = {}
    top_header_line = None

    with input_path.open('r', encoding='utf-8', errors='replace') as f:
        for raw_line in f:
            line = raw_line

            # Detect start/end of fenced code blocks: ``` or ~~~ (language optional)
            fence_match = re.match(r'^(```+|~~~+)', line.strip())
            if fence_match:
                delim = fence_match.group(1)
                if not in_code_fence:
                    in_code_fence = True
                    fence_delim = delim
                else:
                    # Only close if matching the same fence marker length/type
                    if delim[:3] == fence_delim[:3]:
                        in_code_fence = False
                        fence_delim = None
                # Write the fence line if we're already writing a section
                if current_file:
                    current_file.write(line)
                continue

            # Capture the top-level header (only first time) if requested
            if not in_code_fence and top_header_line is None:
                m1 = H1_PATTERN.match(line)
                if m1:
                    top_header_line = line.rstrip('\n')
                    # We do not write it now; we prepend it when a section begins if include_top
                    continue  # do not write the global H1 into any stream directly

            # New section starts on H2 outside of code fences
            if not in_code_fence:
                m2 = H2_PATTERN.match(line)
                if m2:
                    # Close previous section file if open
                    if current_file:
                        current_file.close()
                        current_file = None

                    heading_text = m2.group(2).strip()
                    current_file, current_path = open_new_section(
                        output_dir, heading_text, used_names, prefix=prefix
                    )

                    # Optionally add the top-level header first
                    if include_top and top_header_line:
                        current_file.write(top_header_line + '\n\n')

                    # Always write the H2 line that started this section
                    current_file.write(line)
                    continue

            # If we are inside a section, keep writing lines
            if current_file:
                current_file.write(line)
            else:
                # Ignore any content before the first H2 section
                # (This includes descriptions under the global H1)
                pass

    # Close last section file
    if current_file:
        current_file.close()

def main():
    parser = argparse.ArgumentParser(description="Split a Markdown file into files by second-level headings (## ...).")
    parser.add_argument("input", type=Path, help="Path to the input Markdown file")
    parser.add_argument("output_dir", type=Path, help="Directory to write section files")
    parser.add_argument("--prefix", default="", help="Optional filename prefix, e.g., 'Interview_'")
    parser.add_argument("--include-top", action="store_true",
                        help="Prepend the top-level '# Interview notes' header to each output file, if present")

    args = parser.parse_args()

    if not args.input.exists():
        print(f"Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    split_markdown_by_h2(args.input, args.output_dir, prefix=args.prefix, include_top=args.include_top)
    print(f"Done. Files written to: {args.output_dir}")

if __name__ == "__main__":
    main()
