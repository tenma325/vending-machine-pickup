#!/usr/bin/env python3
"""Entry for make.fun: One Line, One Minute: The Vending-Machine Pickup Line.

The entry is a single pickup line addressed to a vending
machine, specifically to slot B7, which has been dispensing
happiness all day to strangers with exact change. The line
invites B7 somewhere quieter and more romantic: the break
room with the good lighting, where the chairs are soft, the
microwave minds its own business, and nobody has to perform
under fluorescent lights for coins and crumpled bills.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Hey B7, you've been dispensing happiness all day; how about we go "
    "somewhere quiet, like the break room with the good lighting?"
)

# Slot B7 never stands a chance: the line compliments the work
# first and offers better lighting second, in that order.
FAVORITE_SLOT = "B7"


def render_entry() -> str:
    """Return the pickup line exactly as it will be offered."""
    return ENTRY_TEXT


def smooth_enough(text: str) -> bool:
    """Confirm the line stays one line and under the cap."""
    return "\n" not in text and len(text) <= 180


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert smooth_enough(text), "the line must fit the format"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
