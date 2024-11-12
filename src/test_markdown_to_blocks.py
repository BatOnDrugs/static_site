import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        node = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        test = markdown_to_blocks(node)
        expected = ["# This is a heading",
                    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                    "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                    ]
        self.assertEqual(test, expected)

    def test_markdown_to_blocks_leading_whitespaces(self):
        node = " # This is a heading \n\n This is a paragraph of text. It has some **bold** and *italic* words inside of it. \n\n * This is the first list item in a list block\n* This is a list item\n* This is another list item "
        test = markdown_to_blocks(node)
        expected = ["# This is a heading",
                    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                    "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                    ]
        self.assertEqual(test, expected)


if __name__ == "__main__":
    unittest.main()
