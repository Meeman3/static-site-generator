
import os
import shutil
from src.page_generator import generate_pages_recursive


def main():

    if os.path.exists("./public/"):
        shutil.rmtree("./public/")

    dir_copy("./static/", "./public/")

    generate_pages_recursive("./content/", "./template.html", "./public/")

def dir_copy(src_dir, dst_dir):
    os.mkdir(dst_dir)

    
    src_path = src_dir
    dst_path = dst_dir

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            
        else:
            dir_copy(src_path, dst_path)







main()