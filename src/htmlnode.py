class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props =  props


    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):

        prop_html = ""

        for attribute in self.props.keys():
            prop_html += " " + attribute + f'="{self.props[attribute]}"'

        return prop_html
    
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"