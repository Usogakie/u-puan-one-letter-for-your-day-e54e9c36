"""One Letter for Your Day.

Writes exactly one letter to the output directory: Z.

Z stands for the word behind the day: zombie. A day spent
shuffling through everything on autopilot, half asleep, running
on nothing -- vivid, funny, and honest. Zero sleep, zombie mode.
"""

import os


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one character, no trailing newline: the gate wants
    # 1 to 1 characters, and a newline would make it 2 bytes.
    with open(path, "w", encoding="utf-8") as f:
        f.write("Z")


if __name__ == "__main__":
    main()
