import unittest

from textnode import TextNode
from textnode_regex import (extract_markdown_images,extract_markdown_links)


class TestTextNodeRegex(unittest.TestCase):
    def test_regex_normal(self):
        self.assertEqual(extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"),[("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])
        self.assertEqual(extract_markdown_links("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"),[("link", "https://www.example.com"), ("another", "https://www.example.com/another")])
 

    if __name__ == "__main__":
     unittest.main()