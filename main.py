"""One Word for the Boss -- entry program.

Writes exactly one word describing the boss to entry.txt.

The word: Seagull.
A "seagull manager" flies in, makes a lot of noise, dumps on everyone,
and flies out again. It is a single word people actually use about the
boss they report to, it lands on its own without a caption, it catches
a real and widely met boss habit, it is fresh (not the first word anyone
reaches for), and it travels across kitchens, warehouses and offices.
Seven characters, so it also wins the size tie-break against longer words.
"""

import os
import sys

WORD = "Seagull"


def main() -> int:
    # Gate check, same rule the sealed scorer applies: 1-30 characters,
    # a single word, not only whitespace. Fail loudly instead of
    # silently writing an entry that could never be judged.
    if not (1 <= len(WORD) <= 30):
        raise ValueError("word must be 1-30 characters")
    if len(WORD.split()) != 1 or WORD != WORD.strip():
        raise ValueError("entry must be exactly one word")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
