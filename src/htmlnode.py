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

class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,props=None):
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