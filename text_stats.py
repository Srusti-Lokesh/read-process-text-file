"""Core text-file statistics logic.

The implementation processes files line-by-line so that a large text file
does not need to be loaded completely into memory.
"""

from __future__ import annotations

from pathlib import Path
from typing import BinaryIO, TextIO


def _count_lines(stream: TextIO) -> dict[str, int]:
    line_count = 0
    word_count = 0
    character_count = 0

    for line in stream:
        line_count += 1
        # Character count excludes line-ending characters.
        character_count += len(line.rstrip("\r\n"))
        word_count += len(line.split())

    return {
        "line_count": line_count,
        "word_count": word_count,
        "character_count": character_count,
    }


def process_file(file_path: str | Path, encoding: str = "utf-8") -> dict[str, int]:
    """Read a local text file safely and return line/word/character counts."""
    with open(file_path, "r", encoding=encoding) as file:
        return _count_lines(file)


def process_uploaded_file(stream: BinaryIO, encoding: str = "utf-8") -> dict[str, int]:
    """Process an uploaded binary stream incrementally."""
    import io

    text_stream = io.TextIOWrapper(stream, encoding=encoding, newline="")
    try:
        return _count_lines(text_stream)
    finally:
        # Do not close the underlying request stream here.
        text_stream.detach()


def format_statistics(stats: dict[str, int]) -> str:
    """Return statistics in a simple CLI-friendly format."""
    return (
        f"Lines: {stats['line_count']}\n"
        f"Words: {stats['word_count']}\n"
        f"Characters: {stats['character_count']}"
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Read a text file and generate line, word, and character statistics."
    )
    parser.add_argument("file", help="Path to a UTF-8 .txt file")
    args = parser.parse_args()

    try:
        print(format_statistics(process_file(args.file)))
    except FileNotFoundError:
        parser.error(f"File not found: {args.file}")
    except UnicodeDecodeError:
        parser.error("The file is not valid UTF-8 text.")
