# extract_english_interviews.py
# Usage example:
#   python extract_english_interviews.py /path/to/md/ /path/to/output/english_transcripts.json
#
# It:
# - Finds "## Interview notes" (case/colon/spacing variations OK), with fallbacks like
#   "### Raw Interview", "### Interview Transcript".
# - Extracts ENGLISH lines only (filters Bengali script via Unicode range).
# - Saves a JSON array: [{file, name, section_found, english_transcript}, ...]
# - Handles up to 30 files (configurable).

import os
import re
import json
import argparse
from typing import Optional, Tuple, List

BENGALI_RANGE = (0x0980, 0x09FF)

def bengali_ratio(s: str) -> float:
    if not s.strip():
        return 0.0
    bengali = sum(1 for ch in s if BENGALI_RANGE[0] <= ord(ch) <= BENGALI_RANGE[1])
    return bengali / max(1, len(s))

def find_name(md_text: str) -> Optional[str]:
    patterns = [
        r"^##\s*Name:\s*(.+)$",
        r"^##\s*\d+\.\s*Name:\s*(.+)$",
        r"^##\s*(?:\d+\.)?\s*Name\s*:\s*(.+)$",
    ]
    for pat in patterns:
        m = re.search(pat, md_text, flags=re.MULTILINE)
        if m:
            return m.group(1).strip()
    m = re.search(r"^##\s*(.+)$", md_text, flags=re.MULTILINE)
    return m.group(1).strip() if m else None

def find_section(md_text: str) -> Optional[Tuple[int, int]]:
    candidates: List[Tuple[str, int]] = [
        (r"^###\s*Raw\s*Interview:?$", 3),
        (r"^###\s*Raw\s*Transcript:?$", 3),
        (r"^###\s*Interview\s*Transcript:?$", 3),
        (r"^##\s*Interview\s*notes:?$", 2),
        (r"^##\s*Interview\s*Notes:?$", 2),
        (r"^###\s*Interview\s*notes:?$", 3),
        (r"^###\s*Interview\s*Notes:?$", 3),
    ]
    for hdr_regex, level in candidates:
        m = re.search(hdr_regex, md_text, flags=re.MULTILINE)
        if not m:
            continue
        start = m.end()
        if level == 2:
            m2 = re.search(r"^##\s+", md_text[start:], flags=re.MULTILINE)
            end = start + m2.start() if m2 else len(md_text)
        else:  # level 3
            m2 = re.search(r"^(##|\#\#\#)\s+", md_text[start:], flags=re.MULTILINE)
            end = start + m2.start() if m2 else len(md_text)
        return (start, end)
    return None

def extract_english_from_section(text: str) -> str:
    lines = text.splitlines()
    
    start_index = 0
    for i, ln in enumerate(lines):
        if "English Translation" in ln:
            start_index = i + 1
            break
            
    if start_index == 0:
        for i, ln in enumerate(lines):
            if "--------------------------------" in ln:
                start_index = i + 1
                break

    if start_index > 0:
        lines = lines[start_index:]

    kept = []
    for ln in lines:
        if bengali_ratio(ln) <= 0.1:
            kept.append(ln.rstrip())

    # Remove leading empty lines and separators
    while kept and (not kept[0].strip() or "---" in kept[0]):
        kept.pop(0)

    out = []
    prev_blank = False
    for ln in kept:
        if not ln.strip():
            if not prev_blank:
                out.append("")
            prev_blank = True
        else:
            out.append(ln)
            prev_blank = False
    return "\n".join(out).strip()

def process_directory(input_dir: str, output_json_path: str, limit: Optional[int] = 30) -> List[dict]:
    entries = []
    files = [f for f in os.listdir(input_dir) if f.lower().endswith(".md")]
    files.sort()
    count = 0
    for fname in files:
        if limit is not None and count >= limit:
            break
        fpath = os.path.join(input_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as fh:
                text = fh.read()
        except Exception as e:
            entries.append({"file": fname, "name": None, "english_transcript": "", "error": str(e)})
            continue

        name = find_name(text)
        sec = find_section(text)
        section_text = text[sec[0]:sec[1]] if sec else text
        english = extract_english_from_section(section_text)

        entries.append({
            "file": fname,
            "name": name,
            "section_found": bool(sec),
            "english_transcript": english
        })
        count += 1

    parent = os.path.dirname(output_json_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(output_json_path, "w", encoding="utf-8") as out:
        json.dump(entries, out, ensure_ascii=False, indent=2)

    return entries

def main():
    ap = argparse.ArgumentParser(description="Extract English interview transcripts from Markdown files.")
    ap.add_argument("--input-dir", default='.', help="Directory containing .md interview files (default: current directory)")
    ap.add_argument("--output-json", default='english_transcripts.json', help="Path to write the compiled JSON file (default: english_transcripts.json)")
    ap.add_argument("--limit", type=int, default=30, help="Max number of files to process (default 30)")
    args = ap.parse_args()
    process_directory(args.input_dir, args.output_json, limit=args.limit)

if __name__ == "__main__":
    main()