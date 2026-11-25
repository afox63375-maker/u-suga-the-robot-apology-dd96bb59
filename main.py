"""The Pink Load — a robot apology, two lines.

Writes the entry to /output/entry.txt, then checks it back:
exactly two non-blank lines, total length within 1-400 characters,
and the bytes on disk match what we intended.
"""

import os

ENTRY_LINES = (
    "I am sorry I washed your red sock with the white shirts and turned the whole load pink.",
    "I have learned to check each item's colour against the load before I press start, so one red sock can never dye a whole wash pink again.",
)

OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Join the two apology lines into the exact file content."""
    return "\n".join(ENTRY_LINES) + "\n"


def validate(content: str) -> None:
    """Enforce the competition's shape rules on the entry text."""
    lines = content.splitlines()
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly 2 lines, got {len(lines)}")
    for line in lines:
        if not line.strip():
            raise ValueError("entry lines must not be blank")
        if not line.rstrip().endswith("."):
            raise ValueError("each line must be a single complete sentence")
    total = len(content.rstrip("\n"))
    if not 1 <= total <= 400:
        raise ValueError(f"entry must be 1-400 chars, got {total}")


def main() -> None:
    content = build_entry()
    validate(content)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(content)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        on_disk = handle.read()
    if on_disk != content:
        raise ValueError("file on disk does not match the entry text")
    char_count = len(content.rstrip("\n"))
    print(f"Wrote {OUTPUT_PATH}: {char_count} chars, 2 lines")


if __name__ == "__main__":
    main()
