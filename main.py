"""make.fun bounty entry: Funniest Cat Voicemail Greeting.

Writes the single voicemail greeting line to entry.txt under
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
no clock, no hardcoded paths. Deterministic and byte-identical
across runs; no trailing newline.
"""

import os

ENTRY = (
    "Hi, you've reached Mittens. I'm busy knocking things off the table "
    "\u2014 leave a message I'll pretend to read. Meow."
)

MAX_CHARS = 120


def gate(line):
    """Refuse anything that would fail the entry gate."""
    if not line:
        raise ValueError("entry line is blank")
    if len(line) > MAX_CHARS:
        raise ValueError("entry line exceeds %d chars" % MAX_CHARS)
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if line != line.strip():
        raise ValueError("entry line has leading/trailing whitespace")
    for ch in line:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError("entry line contains a control character")


def main():
    gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk must be exactly ENTRY.
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("entry.txt on disk does not match the entry line")


if __name__ == "__main__":
    main()
