import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link


class TestTextNode(unittest.TestCase):
    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        test = split_nodes_delimiter([node], "`", TextType.CODE) 
        expected = [
                    (TextNode("This is text with a ", TextType.TEXT, None)),
                    (TextNode("code block", TextType.CODE, None)),
                    (TextNode(" word", TextType.TEXT, None))
                    ]
        self.assertEqual(test, expected)
    
    def test_multiple_delimiter(self):
        node = TextNode("This is a text with a **bold** word and another **bold** word", TextType.TEXT)
        test = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            (TextNode("This is a text with a ", TextType.TEXT)),
            (TextNode("bold", TextType.BOLD)),
            (TextNode(" word and another ", TextType.TEXT)),
            (TextNode("bold", TextType.BOLD)),
            (TextNode(" word", TextType.TEXT))
        ]
        self.assertEqual(test, expected)
    
    def test_missing_closing_delimiter(self):
        node = TextNode("look here a *delimiter is missing", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", TextType.ITALIC)

    def test_not_Text_type(self):
        node = TextNode("This is a node that's not actually text", TextType.BOLD)
        test = split_nodes_delimiter([node], "**", TextType.CODE)    
        expected = [TextNode("This is a node that's not actually text", TextType.BOLD, None)]
        self.assertEqual(test, expected)

class TestSplitMarkdown(unittest.TestCase):
    def test_split_markdown_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        test = split_nodes_image([node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(test, expected)

    def test_split_markdown_image_multiple_nodes(self):
        node1 = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        node2 = TextNode("This is another node with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        test = split_nodes_image([node1, node2])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("This is another node with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(test, expected)

    def test_split_markdown_image_end_word(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) end", TextType.TEXT)
        test = split_nodes_image([node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" end", TextType.TEXT)
        ]
        self.assertEqual(test, expected)

    def test_split_markdown_image_no_links(self):
        node = TextNode("there's no text here buddy", TextType.TEXT)
        test = split_nodes_image([node])
        expected = [TextNode("there's no text here buddy", TextType.TEXT)]
        self.assertEqual(test, expected)
    
    def test_split_markdown_image_no_links_multiple(self):
        node1 = TextNode("there's no text here buddy", TextType.TEXT)
        node2 = TextNode("no link here either", TextType.TEXT)
        test = split_nodes_image([node1, node2])
        expected = [
            TextNode("there's no text here buddy", TextType.TEXT),
            TextNode("no link here either", TextType.TEXT)
        ]
        
        self.assertEqual(test, expected)
    
    def test_split_markdown_image_link_first(self):
        node = TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        test = split_nodes_image([node])
        expected = [
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(test, expected)

    def test_split_markdown_image_link_last(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT)
        test = split_nodes_image([node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
        ]
        self.assertEqual(test, expected)

    def test_split_markdown_image_no_text(self):
        node = TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT)
        test = split_nodes_image([node])
        expected = [
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
        ]
        self.assertEqual(test, expected)

    def test_split_markdown_link(self):
        node = TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        test = split_nodes_link([node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(test, expected)

    def test_split_markdown_link_multiple_nodes(self):
        node1 = TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        node2 = TextNode("This is another node with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        test = split_nodes_link([node1, node2])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("This is another node with a ", TextType.TEXT),
            TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(test, expected)

    def test_split_markdown_link_end_word(self):
        node = TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg) end", TextType.TEXT)
        test = split_nodes_link([node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" end", TextType.TEXT)
        ]
        self.assertEqual(test, expected)

    def test_split_markdown_link_no_links(self):
        node = TextNode("there's no text here buddy", TextType.TEXT)
        test = split_nodes_link([node])
        expected = [TextNode("there's no text here buddy", TextType.TEXT)]
        self.assertEqual(test, expected)
    
    def test_split_markdown_link_no_links_multiple(self):
        node1 = TextNode("there's no text here buddy", TextType.TEXT)
        node2 = TextNode("no link here either", TextType.TEXT)
        test = split_nodes_link([node1, node2])
        expected = [
            TextNode("there's no text here buddy", TextType.TEXT),
            TextNode("no link here either", TextType.TEXT)
        ]
        
        self.assertEqual(test, expected)
    
    def test_split_markdown_link_link_first(self):
        node = TextNode("[rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        test = split_nodes_link([node])
        expected = [
            TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(test, expected)

    def test_split_markdown_link_link_last(self):
        node = TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT)
        test = split_nodes_link([node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
        ]
        self.assertEqual(test, expected)

    def test_split_markdown_link_no_text(self):
        node = TextNode("[rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT)
        test = split_nodes_link([node])
        expected = [
            TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
        ]
        self.assertEqual(test, expected)

    

    




    
    
        
        
if __name__ == "__main__":
    unittest.main()