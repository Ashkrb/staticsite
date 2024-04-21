import unittest

from textnode import TextNode
from textnode_regex import (extract_markdown_images,extract_markdown_links)
from textnode_split import text_to_textnodes




class TestTextNodeRegex(unittest.TestCase):
    def test_regex_normal(self):
        self.assertEqual(extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"),[("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])
        self.assertEqual(extract_markdown_links("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"),[("link", "https://www.example.com"), ("another", "https://www.example.com/another")])
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", "text"),
                TextNode("text", "bold"),
                TextNode(" with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word and a ", "text"),
                TextNode("code block", "code"),
                TextNode(" and an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", "text"),
                TextNode("link", "link", "https://boot.dev"),
            ],
            nodes,
        )

    if __name__ == "__main__":
     unittest.main()