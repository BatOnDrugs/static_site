import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_HTMLNode(self):
        node = {"hotel": "Trivago"}
        print(HTMLNode(node).props_to_html())
        node = None, {"hotel": "Trivago"}
        print(HTMLNode(node).props_to_html())
        node = None
        print(HTMLNode(node).props_to_html())
        


if __name__ == "__main__":
    unittest.main()