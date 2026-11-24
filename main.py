"""Weirdest Job Title entry: one fixed job title, nothing else.

The grader runs this program twice with no network; both runs must write
the same bytes to the output file. The title is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

The title: "Professional Mourner for Strangers' Goldfish".

Why this one: a professional mourner is a real job (hired mourners exist),
so the frame sounds real, and the twist is one hilariously specific
detail -- the deceased is a stranger's goldfish. It paints an instant
picture (a stranger weeping at a tiny fish funeral) instead of a generic
oddity like "Chief Weirdness Officer", and it is not a joke format the
board has already seen: no geese, no socks, no "Vice President of"
punchline.
"""

import os


TITLE = "Professional Mourner for Strangers' Goldfish"

# The competition allows a single job title of at most 60 characters.
MAX_CHARS = 60


def output_path() -> str:
    # The output directory is owned by the grader: never delete or
    # recreate it, only create it when it does not already exist.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    text = TITLE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "title must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("title must be a single line")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the title.
    with open(path, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the title")
    print(text)


if __name__ == "__main__":
    main()
