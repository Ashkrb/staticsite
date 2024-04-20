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

