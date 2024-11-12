import unittest

from htmlnode import *


class TestParentNode(unittest.TestCase):
    def test_parent_node_with_tag_and_children(self):
        parent = ParentNode("div", [
            ParentNode("p", [
            LeafNode("b", "Hello")
            ])
            ])
        self.assertEqual(parent.to_html(), "<div><p><b>Hello</b></p></div>")

    def test_parent_node_without_tag(self):
        with self.assertRaises(ValueError):
            parent = ParentNode([
            ParentNode("p", [
            LeafNode("b", "Hello")
            ])
            ])
            parent.to_html()
    def test_parent_node_without_children(self):
        with self.assertRaises(ValueError):
            parent = ParentNode("div", [
            ParentNode("p", 
            )
            ])
            parent.to_html()
    def test_example_from_boot(self):
        parent = ParentNode(
        "p",
        [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ],
        )
        print(parent.to_html())
        self.assertEqual(parent.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
        


if __name__ == "__main__":
    unittest.main()