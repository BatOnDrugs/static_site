from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue
        elif not node.text:
            continue
        elif delimiter not in node.text:
            new_node.append(node)

        else:
            segment_list = node.text.split(delimiter)
            for index, segment in enumerate(segment_list):
                if index % 2 == 0:
                    new_node.append(TextNode(segment, TextType.TEXT))
                else:
                    new_node.append(TextNode(segment, text_type))
            if len(segment_list) < 3:
                raise Exception("missing closing delimiter")

    return new_node

def split_nodes_image(old_nodes):
    new_node = []  
    for node in old_nodes:    
        text_copy = node.text
        segment_list = extract_markdown_images(text_copy)
        
        if not text_copy:
            continue
        elif segment_list == []:       
            new_node.append(node)
            continue               

                 

        for segment in segment_list:
            delimiter = f"![{segment[0]}]({segment[1]})"
            parts = text_copy.split(delimiter, 1)
            before_image = parts[0]
            after_image = parts[1]
            if before_image != "":
                new_node.append(TextNode(before_image, TextType.TEXT))
                new_node.append(TextNode(segment[0], TextType.IMAGE, segment[1]))
            else:
                new_node.append(TextNode(segment[0], TextType.IMAGE, segment[1]))
            text_copy = after_image
       
        if after_image != "":
            new_node.append(TextNode(after_image, TextType.TEXT))
   
    return new_node

def split_nodes_link(old_nodes):
    new_node = []  
    for node in old_nodes:    
        text_copy = node.text
        segment_list = extract_markdown_links(text_copy)
        if not text_copy:
            continue
        elif segment_list == []:       
            new_node.append(node)
            continue                       

        for segment in segment_list:
            delimiter = f"[{segment[0]}]({segment[1]})"
            parts = text_copy.split(delimiter, 1)
            before_link = parts[0]
            after_link = parts[1]
            if before_link != "":
                new_node.append(TextNode(before_link, TextType.TEXT))
                new_node.append(TextNode(segment[0], TextType.LINK, segment[1]))
            else:
                new_node.append(TextNode(segment[0], TextType.LINK, segment[1]))
            text_copy = after_link
       
        if after_link != "":
            new_node.append(TextNode(after_link, TextType.TEXT))
           
    return new_node




