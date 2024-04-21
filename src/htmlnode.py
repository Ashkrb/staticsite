from textnode import TextNode
class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

#tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
#value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
#children - A list of HTMLNode objects representing the children of this node
#props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

#An HTMLNode without a tag will just render as raw text
#An HTMLNode without a value will be assumed to have children
#An HTMLNode without children will be assumed to have a value
#An HTMLNode without props simply won't have any attributes

    def to_html(self):
       raise NotImplementedError
    
    #children will implement this

    def props_to_html(self):
        represent_string = ""
        if self.props is not None:
             
            for item in self.props:
                represent_string += f' {item}="{self.props[item]}"'
        return represent_string
    
    def __repr__(self):
        print(f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props_to_html()})")
    def text_node_to_html_node(text_node):
         if text_node.text_type == "text":
              return LeafNode(None,text_node.text)
         elif text_node.text_type == "bold":
              return LeafNode("b",text_node.text)
         elif text_node.text_type == "italic":
              return LeafNode("i",text_node.text)
         elif text_node.text_type == "code":
              return LeafNode("code",text_node.text)
         elif text_node.text_type == "link":
              props = {"href": text_node.url}
              return LeafNode("a",text_node.text,props)
         elif text_node.text_type == "image":
              props = {"src": text_node.url, "alt": text_node.text}
              return LeafNode("img","",props)
         else:
              raise Exception("not valid type")

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
                super().__init__(tag,value,props)
                

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf has no value")
        properties = self.props_to_html()
        if self.tag is None:
             return self.value
        
        return (f"<{self.tag}{properties}>{self.value}</{self.tag}>")
    
    def __repr__(self):
         return f"LeadNode({self.tag}{self.value}{self.props})"
    


class ParentNode(HTMLNode):
         def __init__(self, tag,children, props=None):
              super().__init__(tag, None, children, props)

         def to_html(self):
            childrentext = ""
            if self.tag == None:
                 raise ValueError("no tag")
            if len(self.children) == 0:
                 raise ValueError("no children")
            
            for item in self.children:
                 childrentext += item.to_html()
            
            textform = f"<{self.tag}{self.props_to_html()}>{childrentext}</{self.tag}>"
            return textform
         
         def __repr__(self):
             return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
            