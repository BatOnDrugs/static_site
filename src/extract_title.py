from markdown_to_blocks import markdown_to_blocks
def extract_title(markdown):
    if markdown_to_blocks(markdown)[0][:2] == "# ":
        return markdown_to_blocks(markdown)[0].lstrip("# ")
    else:
        raise Exception("No h1 header")
    
