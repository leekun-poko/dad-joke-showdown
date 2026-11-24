#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes the entry joke to ``entry.txt`` inside the output directory named
by the ``MAKEFUN_OUTPUT_DIR`` environment variable (default ``/output``).
Python 3.13, standard library only, no network access.
"""

import os
from pathlib import Path

ENTRY_TEXT = "What do you call a factory that makes okay products? A satisfactory."
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"

def resolve_output_dir() -> Path:
    """Return the output directory, honouring $MAKEFUN_OUTPUT_DIR."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))


def main() -> None:
    target_dir = resolve_output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    entry_path = target_dir / OUTPUT_FILENAME
    entry_path.write_text(ENTRY_TEXT, encoding="utf-8")
    print(f"Wrote entry to {entry_path}")


if __name__ == "__main__":
    main()
