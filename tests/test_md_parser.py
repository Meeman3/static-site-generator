import unittest

from src.page_generator import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_trims_whitespace(self):
        self.assertEqual(extract_title("   #   Hello World   \n"), "Hello World")

    def test_ignores_other_headers(self):
        md = "## Not this\nSome text\n# The One\nMore text"
        self.assertEqual(extract_title(md), "The One")

    def test_requires_single_hash_and_space(self):
        md = "### Not it\n#Title without space\n#### Also not it\n# Yes this one"
        self.assertEqual(extract_title(md), "Yes this one")

    def test_multiline_content(self):
        md = "# Title\n\nParagraph\n- list"
        self.assertEqual(extract_title(md), "Title")

    def test_raises_when_missing(self):
        with self.assertRaises(Exception):
            extract_title("No header here\n## Subheader\ntext")

if __name__ == "__main__":
    unittest.main()