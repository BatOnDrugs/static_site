class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())
    
    def __eq__(self, other):
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        return f"HTMLNode(tag={self.tag} value={self.value} children={self.children} props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props = None):
        super().__init__(tag, value, None, props)
        if self.value == None:
            raise ValueError
        
    def to_html(self):
        if not self.tag:
            return f"{self.value}"
        elif not self.props:
            self.props = {}    
        
        attributes = ''.join(f' {key}="{value}"' for key, value in (self.props or {}).items())
        return f'<{self.tag}{attributes}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        super().__init__(tag, None,  children, props)
    
    def to_html(self):
        
        if not self.tag:
            raise ValueError("no tag")
        if not self.children:
            raise ValueError("no children")
        children_nodes = ""
        for child in self.children:
            children_nodes += child.to_html()
        return f"<{self.tag}>{children_nodes}</{self.tag}>"
            
            
        
        
        
        





def main():
    tag = "a"
    value = "I like it"
    props = {
    "href": "https://www.google.com", 
    "target": "_blank",
    }   
    print((LeafNode(tag, value, None)).to_html())


    

if __name__ == "__main__":
    main()

    


        
    
