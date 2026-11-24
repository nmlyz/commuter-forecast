#!/usr/bin/env python3
"""Write one weather forecast line to /output/entry.txt.

The line is a single sentence of at most 140 characters: a forecast for
an invented city, Mizzleham, where the drizzle is so light the forecast
The output is fixed text: running the program twice writes byte-identical
output, and the file is left readable by every user (mode 0644).
"""

import os
import stat

LINE = (
    "Mizzleham: drizzle so light the forecast calls it "
    "'atmospheric moisture'; your hair calls it betrayal."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    assert 1 <= len(text) <= 140, "entry must be 1 to 140 characters"
    assert "\n" not in text, "entry must be one line"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    os.umask(0o022)
    main()
