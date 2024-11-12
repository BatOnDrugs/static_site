import unittest
from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode
from textnode import TextNode, TextType

class TestMarkdownToHTMLNode(unittest.TestCase):
    
    def test_markdown_to_html_node_heading(self):

        node = """# Heading\n## Heading 2"""
        test = markdown_to_html_node(node)
        expected = HTMLNode("div", value=None, children=[HTMLNode("h1", [TextNode("Heading", TextType.TEXT)]), HTMLNode("h2", [TextNode("Heading 2", TextType.TEXT, None)])])
        self.assertEqual(test, expected)
    
    


if __name__ == "__main__":
    unittest.main()
        
