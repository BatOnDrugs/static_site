from htmlnode import *
from block_to_block_type import block_to_block_type
from conversion import text_node_to_html_node
from text_to_text_nodes import text_to_textnodes
from markdown_to_blocks import markdown_to_blocks
from textnode import *
from string import digits


# 1. split the text to blocks and figure out the block types.
# 2. depending on the block type create HTMLNode with proper data attached
# 3. take those HTMLNodes and format them into inline markdown




def markdown_to_html_node(markdown): # takes a markdown text and turns it into an html node through some fuckery and text_node_to_html_node
    result = []
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        result.append(text_to_children(block))
    node = ParentNode("div", result)
    return node
    


            

def text_to_children(block):
    if block_to_block_type(block) == "heading":
        node_list = []
        hash_count = 0
        tag = ""
        hashes = ""
        for i in range(5):
            if block[i] == "#":
                hash_count += 1
                hashes += "#"
        tag = f"h{hash_count}"
        return text_node_lists_to_html(tag, text_to_textnodes(block.lstrip(f"{hashes}").lstrip(" ")))
    elif block_to_block_type(block) == "quote":
        return text_node_lists_to_html("blockquote", text_to_textnodes(block.replace("> ", "")))
    elif block_to_block_type(block) == "unordered_list":
        return list_to_parent_node("ul", block)
    elif block_to_block_type(block) == "ordered_list":
        return list_to_parent_node("ol", block)
    elif block_to_block_type(block) == "paragraph":
        return text_node_lists_to_html("p", text_to_textnodes(block))
    elif block_to_block_type(block) == "code":
        block = handle_code_block(block)
        return ParentNode("pre", [text_node_lists_to_html("code", text_to_textnodes(block))])
        

def list_to_parent_node(tag, block):
    line_list = block.split("\n")
    leaf_nodes = []
    for line in line_list:
        leaf_nodes.append(text_node_lists_to_html("li", text_to_textnodes(line.lstrip(f"{digits}. ").lstrip("* ").lstrip("- "))))
    return ParentNode(tag, leaf_nodes)

def handle_code_block(block):
    lines = block.split("\n")
    lines[0] = "```"
    return "\n".join(lines)

def text_node_lists_to_html(tag, text_node_list):
    result = []
    for item in text_node_list:
        result.append(text_node_to_html_node(item))
    return ParentNode(tag, result)







