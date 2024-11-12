import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Use with statements to properly handle files
    with open(from_path, "r") as source_file:
        source = source_file.read()
    
    with open(template_path, "r") as template_file:
        template = template_file.read()
    
    html_content = markdown_to_html_node(source).to_html()
    
    title = extract_title(source)
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    os.makedirs(os.path.dirname(dest_path), exist_ok = True)
    with open(dest_path, "w") as dest_file:
        dest_file.write(final_html)

    
    
    


