from textnode import TextNode
from textnode_regex import (extract_markdown_images,extract_markdown_links)


def split_nodes_image(old_nodes):
    final_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            final_nodes.append(node)
            continue
        nodes_text = node.text
        img_tuples = extract_markdown_images(node.text)
        if len(img_tuples) == 0:
            final_nodes.append(node)
            continue
        for img in img_tuples:
             if img[1] == "" or img[1] is None:
                continue
             section = node.text.split(f"![{img[0]}]({img[1]})", 1)
             if section[0] != "":
                 
                final_nodes.append(TextNode(section[0],"text"))
             final_nodes.append(TextNode(img[0],"image",img[1]))
             nodes_text = section[1]

        if nodes_text != "":
            final_nodes.append(TextNode(nodes_text,"text"))
    return final_nodes

def split_nodes_link(old_nodes):
    final_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            final_nodes.append(node)
            continue
        nodes_text = node.text
        link_tuples = extract_markdown_links(node.text)
        if len(link_tuples) == 0:
            final_nodes.append(node)
            continue
        for lnk in link_tuples:
             if lnk[1] == "" or lnk[1] is None:
                continue
             section = node.text.split(f"[{lnk[0]}]({lnk[1]})", 1)
             if section[0] != "":
                 
                final_nodes.append(TextNode(section[0],"text"))
             final_nodes.append(TextNode(lnk[0],"link",lnk[1]))
             nodes_text = section[1]

        if nodes_text != "":
            final_nodes.append(TextNode(nodes_text,"text"))
    return final_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, "text")]
    nodes = TextNode.split_nodes_delimiter(nodes, "**", "bold")
    nodes = TextNode.split_nodes_delimiter(nodes, "*", "italic")
    nodes = TextNode.split_nodes_delimiter(nodes, "`", "code")
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

