def block_to_block_type(block):
    block_type = ""
    line_list = block.split("\n")
    
    if all(line.startswith("> ") for line in line_list):
        block_type = "quote"

    elif all(line.startswith("* ") for line in line_list) or all(line.startswith("- ") for line in line_list):
        block_type = "unordered_list"

    elif all(line_list[i].startswith(f"{i + 1}. ") for i in range(len(line_list))):
        block_type = "ordered_list"

    elif block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        block_type = "heading"

    elif block.startswith("```") and block.endswith("```"):
        block_type = "code"

    else:
        block_type = "paragraph"
    
    return block_type







