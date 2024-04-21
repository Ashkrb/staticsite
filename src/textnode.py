text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    

    def __eq__(TextNode1,Textnode2):
        if TextNode1.text == Textnode2.text and TextNode1.text_type == Textnode2.text_type and TextNode1.url == Textnode2.url:
            return True
        else:
            return False
        

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != "text":
                new_nodes.append(node)
                continue
            else:
                splitnode = node.text.split(delimiter)
                if len(splitnode) % 2 == 0:
                    raise Exception("invalid markdown")
                for i in range (0,len(splitnode)):
                    if splitnode[i] == "":
                         continue
                    if i % 2 == 1:
                        new_nodes.append(TextNode(splitnode[i],text_type))
                    else:
                        new_nodes.append(TextNode(splitnode[i],"text"))
        return new_nodes

                   
    
        
        

