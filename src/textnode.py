class TextNode:
    def __init__(text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    

    def __eg__(TextNode1,Textnode2):
        if TextNode1.text == Textnode2.text and TextNode1.text_type == Textnode2.text_type and TextNode1.url == Textnode2.url:
            return True
        else:
            return False
        

    def __repr__(self):
        return f"TextNode({self.text}{self.text_type}{self.url})"