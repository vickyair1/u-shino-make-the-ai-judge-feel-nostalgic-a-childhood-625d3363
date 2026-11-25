"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

A deterministic program that writes exactly one childhood-memory sentence
to /output/entry.txt and prints it to stdout.

The line is 172 characters, well under the 280-character gate, a single
line with no trailing newline.
"""

import os

LINE = "My grandfather taught me to whistle through a blade of grass on our walk home from school, and I still pick one up every spring, half expecting him to be walking beside me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: 1..280 chars, exactly one line, no leading/trailing whitespace.
    assert 1 <= len(LINE) <= 280, "line must be 1-280 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip guard: the file on disk must be byte-identical to the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "entry.txt round-trip mismatch"
    print(f"{len(LINE)} chars")
    print(LINE)


if __name__ == "__main__":
    main()
