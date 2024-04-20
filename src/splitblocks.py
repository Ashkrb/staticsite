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