"""Extract structured data from tracking/ markdown files.

Usage:
  python extract_tracking.py <tracking_directory>

Outputs JSON array to stdout:
  [{"date": "2026-06-30", "emotion_score": 6, "emotion_word": "满足", "tags": [...]}, ...]
"""

import sys
import json
import re
from pathlib import Path


def parse_frontmatter(text: str) -> dict:
    """Parse YAML-like frontmatter from markdown text."""
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = {}
    for line in parts[1].strip().split("\n"):
        line = line.strip()
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val.startswith("[") and val.endswith("]"):
                val = [v.strip() for v in val[1:-1].split(",")]
            elif val.isdigit():
                val = int(val)
            fm[key] = val
    return fm


def extract_tracking(directory: str) -> list[dict]:
    """Scan directory for tracking markdown files and extract frontmatter data."""
    results = []
    tracking_dir = Path(directory)
    if not tracking_dir.exists():
        print(f"Directory not found: {directory}", file=sys.stderr)
        return results

    for md_file in sorted(tracking_dir.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm.get("type") != "tracking":
            continue
        results.append({
            "file": md_file.name,
            "date": fm.get("title", ""),
            "emotion_score": fm.get("emotion_score"),
            "emotion_word": fm.get("emotion_word", ""),
            "tags": fm.get("tags", []),
        })

    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_tracking.py <tracking_directory>", file=sys.stderr)
        sys.exit(1)
    data = extract_tracking(sys.argv[1])
    print(json.dumps(data, ensure_ascii=False, indent=2))
