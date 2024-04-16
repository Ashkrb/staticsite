import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p","asd")
        print(node.__repr__())
        


if __name__ == "__main__":
    unittest.main()