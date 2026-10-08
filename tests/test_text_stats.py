import tempfile
import unittest
from pathlib import Path

from text_stats import process_file


class TextStatsTests(unittest.TestCase):
    def test_counts(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.txt"
            path.write_text("Hello world\nPython is useful.\n", encoding="utf-8")
            result = process_file(path)

        self.assertEqual(result["line_count"], 2)
        self.assertEqual(result["word_count"], 5)
        self.assertEqual(result["character_count"], len("Hello world") + len("Python is useful."))

    def test_empty_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "empty.txt"
            path.write_text("", encoding="utf-8")
            result = process_file(path)

        self.assertEqual(result, {
            "line_count": 0,
            "word_count": 0,
            "character_count": 0,
        })


if __name__ == "__main__":
    unittest.main()
