block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"





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
