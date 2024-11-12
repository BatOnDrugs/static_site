import os
from generate_page import generate_page
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    path_list = os.listdir(dir_path_content)
   
    for path in path_list:
        if os.path.isfile(os.path.join(dir_path_content, path)):
            dir_ext = path.replace("md", "html")
            print(os.path.join(dir_path_content, path))
            generate_page(os.path.join(dir_path_content, path), template_path, os.path.join(dest_dir_path, dir_ext))
        else:           
            os.mkdir(os.path.join(dest_dir_path, path))           
            generate_pages_recursive(os.path.join(dir_path_content, path), template_path, os.path.join(dest_dir_path, path))
    
    


    
