block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"
from htmlnode import (HTMLNode, ParentNode, LeafNode)
from textnode import TextNode
from textnode_regex import text_to_textnodes
from htmlnode import text_node_to_html_node






def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    blocks = []
    current_lines = ""
    for line in lines:
        if len(line) == 0:
            if current_lines != "":
                blocks.append(current_lines)
                current_lines = ""
            continue        
        else:
            current_lines+=(line+"\n")
    if len(current_lines) != 0:
        blocks.append(current_lines)
    for i in range (0,len(blocks)):
        blocks[i] = blocks[i].strip()
    return blocks

def block_to_block_type(text):
    if text is None:
        raise Exception("no block found")
    if text[0] == "#":
        newtext = text[:6].lstrip("#")
        if newtext[0] == " ":
            return "heading"
    elif text[0]=="`" and text[1]=="`" and text[2]=="`" and text[-3]=="`" and text[-2]=="`" and text[-1]=="`":
        return "code"
    elif text[0] == ">":
        textlines_quote = text.split("\n")
        quote = True
        for quote_line in textlines_quote:
            if quote_line[0] != ">":
                quote = False
                break
        if quote:
            return "quote"
            
    elif text[0] == "*" or text[0]== "-":
        textlines_list = text.split("\n")
        list = True
        for list_line in textlines_list:
            if len(list_line)<2:
                list = False
                break
            if list_line[1] != " " or (list_line[0] != "*" and list_line[0] != "-"):
                list = False
                break
        if list:
            return "unordered_list"
    elif text[0] == 1 or text[0] == "1":
        textlines_ordered_list = text.split("\n")
        ordered_list = True
        nr = 1
        for ordered_line in textlines_ordered_list:
            if len(ordered_line)<3:
                ordered_list = False
                break
            if ordered_line[0] != str(nr) or ordered_line[1] != "." or ordered_line[2] != " ":
                ordered_list = False
                break
            nr += 1
        if ordered_list:
            return "ordered_list"
    else:
        return "paragraph"
    

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)   



def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)