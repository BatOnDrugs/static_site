import unittest

from conversion import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode


class TestConversion(unittest.TestCase):
    def test_conversion_text(self):
        node = TextNode("this is a text node", TextType.TEXT)
        self.assertEqual(text_node_to_html_node(node), LeafNode(value = "this is a text node"))
    def test_conversion_bold(self):
        node = TextNode("this is a bold node", TextType.BOLD)
        self.assertEqual(text_node_to_html_node(node), LeafNode(tag = "b", value = "this is a bold node"))
    def test_conversion_italic(self):
        node = TextNode("this is an italic node", TextType.ITALIC)
        self.assertEqual(text_node_to_html_node(node), LeafNode(tag = "i", value = "this is an italic node"))
    def test_conversion_code(self):
        node = TextNode("this is a code node", TextType.CODE)
        self.assertEqual(text_node_to_html_node(node), LeafNode(tag = "code", value = "this is a code node"))
    def test_conversion_link(self):
        node = TextNode("this is a link node", TextType.LINK, "www.google.com")
        self.assertEqual(text_node_to_html_node(node), LeafNode(tag = "a", value = "this is a link node", props = {"href": "www.google.com"}))
    def test_conversion_image(self):
        node = TextNode("this is an image node", TextType.IMAGE, "www.google.com/image.png")
        self.assertEqual(text_node_to_html_node(node), LeafNode(tag = "img", value = "", props = {"src": "www.google.com/image.png", "alt": "this is an image node"}))

    
        


if __name__ == "__main__":
    unittest.main()