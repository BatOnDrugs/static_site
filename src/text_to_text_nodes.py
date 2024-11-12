from split_nodes import *

def text_to_textnodes(text):
    text = [TextNode(text, TextType.TEXT)] 
    
    return split_nodes_link(
        split_nodes_image(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter(text, "**", TextType.BOLD), "*", TextType.ITALIC), "`", TextType.CODE)))   

