import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_extract_title_h1(self):
        markdown = "# Hello"
        test = extract_title(markdown)
        expected = "Hello"
        self.assertEqual(test, expected)

    def test_extract_title_h2(self):
        with self.assertRaises(Exception):
            markdown = "## Hello"
            extract_title(markdown)

    def test_extract_title_no_h(self):
        with self.assertRaises(Exception):
            markdown = "I like trains"
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()