from textnode import TextNode
import re


def extract_markdown_images(text):
    list_of_images = []
    if text == "" or text is None:
        raise Exception("empty or non existent input text")
    substrings = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    if len(substrings) == 0:
        return list_of_images
    for item in substrings:
        #splititem = re.split('] | [ | ) | (')
        list_of_images.append((item[0],item[1]))
    return list_of_images

def extract_markdown_links(text):
    list_of_links = []
    if text == "" or text is None:
        raise Exception("empty or non existent input text")
    substrings = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    if len(substrings) == 0:
        return list_of_links
    for item in substrings:
        #splititem = re.split('] | [ | ) | (')
        list_of_links.append((item[0],item[1]))
    return list_of_links
def test_text_to_textnodes(self):
        nodes = TextNode.text_to_textnodes(
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