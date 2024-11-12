import unittest
from text_to_text_nodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    
    def test_text_with_markdown_image_and_links(self):

        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        test = text_to_textnodes(text)
        expected = [
                    TextNode("This is ", TextType.TEXT, None), 
                    TextNode("text", TextType.BOLD, None), 
                    TextNode(" with an ", TextType.TEXT, None), 
                    TextNode("italic", TextType.ITALIC, None), 
                    TextNode(" word and a ", TextType.TEXT, None), 
                    TextNode("code block", TextType.CODE, None),
                    TextNode(" and an ", TextType.TEXT, None),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), 
                    TextNode(" and a ", TextType.TEXT, None), 
                    TextNode("link", TextType.LINK, "https://boot.dev")
                ]
        self.assertEqual(test, expected)

    def test_text_with_markdown_without_links(self):

        text = "This is **text** with an *italic* word and a `code block`"
        test = text_to_textnodes(text)
        expected = [
                    TextNode("This is ", TextType.TEXT, None), 
                    TextNode("text", TextType.BOLD, None), 
                    TextNode(" with an ", TextType.TEXT, None), 
                    TextNode("italic", TextType.ITALIC, None), 
                    TextNode(" word and a ", TextType.TEXT, None), 
                    TextNode("code block", TextType.CODE, None),
                ]
        self.assertEqual(test, expected)
    
    def test_text_with_image_only(self):
        
        text = "![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        test = text_to_textnodes(text)
        expected = [
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(test, expected)

    def test_text_with_link_only(self):

        text = "[rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        test = text_to_textnodes(text)
        expected = [    

            TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(test, expected)

    def test_link_and_image(self):

        text = "[rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        test = text_to_textnodes(text)
        expected = [    

            TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(test, expected)


if __name__ == "__main__":
    unittest.main()
        