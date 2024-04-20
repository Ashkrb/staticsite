import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This","bold")
        node4 = TextNode("This is not","bold")
        self.assertEqual(node, node2)
        self.assertNotEqual(node3,node4)

if __name__ == "__main__":
    unittest.main()