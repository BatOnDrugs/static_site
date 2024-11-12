import unittest
from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_block_to_block_type_heading_1(self):
        node = "# this is a quote with 1 #"
        test = block_to_block_type(node)
        expected = "heading"
        self.assertEqual(test, expected)
    
    def test_block_to_block_type_heading_2(self):
        node = "## this is a quote with 2 #"
        test = block_to_block_type(node)
        expected = "heading"
        self.assertEqual(test, expected)
    
    def test_block_to_block_type_heading_3(self):
        node = "### this is a quote with 3 #"
        test = block_to_block_type(node)
        expected = "heading"
        self.assertEqual(test, expected)

    def test_block_to_block_type_heading_4(self):
        node = "#### this is a quote with 4 #"
        test = block_to_block_type(node)
        expected = "heading"
        self.assertEqual(test, expected)
    
    def test_block_to_block_type_heading_5(self):
        node = "##### this is a quote with 5 #"
        test = block_to_block_type(node)
        expected = "heading"
        self.assertEqual(test, expected)

    def test_block_to_block_type_heading_6(self):
        node = "###### this is a quote with 6 #"
        test = block_to_block_type(node)
        expected = "heading"
        self.assertEqual(test, expected)
    
    def test_block_to_block_type_heading_7(self):
        node = "####### this is a quote with 7 #"
        test = block_to_block_type(node)
        expected = "paragraph"
        self.assertEqual(test, expected)

    def test_block_to_block_type_paragraph(self):
        node = "this is a paragraph"
        test = block_to_block_type(node)
        expected = "paragraph"
        self.assertEqual(test, expected)

    def test_block_to_block_type_code_one_line(self):
        node = "```this is code```"
        test = block_to_block_type(node)
        expected = "code"
        self.assertEqual(test, expected)

    def test_block_to_block_type_code_more_lines(self):
        node = "```this is code\nand also this is code```"
        test = block_to_block_type(node)
        expected = "code"
        self.assertEqual(test, expected)

    def test_block_to_block_type_quote_one_line(self):
        node = "> this is a quote"
        test = block_to_block_type(node)
        expected = "quote"
        self.assertEqual(test, expected)

    def test_block_to_block_type_quote_more_lines(self):
        node = "> this is a quote\n> another quote\n> and yet another quote"
        test = block_to_block_type(node)
        expected = "quote"
        self.assertEqual(test, expected)

    def test_block_to_block_type_unordered_list_star(self):
        node = "* this is a list item\n* this is also a list item"
        test = block_to_block_type(node)
        expected = "unordered_list"
        self.assertEqual(test, expected)

    def test_block_to_block_type_unordered_list_dash(self):
        node = "- this is a list item\n- this is also a list item"
        test = block_to_block_type(node)
        expected = "unordered_list"
        self.assertEqual(test, expected)
    
    def test_block_to_block_type_ordered_list(self):
        node = "1. this is a list item\n2. this is also a list item\n3. and a third item"
        test = block_to_block_type(node)
        expected = "ordered_list"
        self.assertEqual(test, expected)

    def test_block_to_block_type_ordered_list_wrong(self):
        node = "1. this is a list item\n4. this is also a list item\n3. and a third item"
        test = block_to_block_type(node)
        expected = "paragraph"
        self.assertEqual(test, expected)

    def test_block_to_block_type_paragraph(self):
        node = "1. this is a list item\n> shoobidoo"
        test = block_to_block_type(node)
        expected = "paragraph"
        self.assertEqual(test, expected)

    
    

if __name__ == "__main__":
    unittest.main()       
