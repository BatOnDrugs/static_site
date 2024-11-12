def markdown_to_blocks(markdown):
    block_list = []
    markdown_lines = markdown.split("\n\n")
    for line in markdown_lines:
        new_line = line.lstrip().rstrip()
        if new_line == "":
            continue
        else:           
            block_list.append(new_line)

       
    return block_list


