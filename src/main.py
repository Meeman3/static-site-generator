
import os
import shutil
from src.page_generator import generate_pages_recursive
import sys


def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    if not basepath.startswith("/"):
        basepath = "/" + basepath
    if not basepath.endswith("/"):
        basepath += "/"

    if os.path.exists("./docs/"):
        shutil.rmtree("./docs/")

    dir_copy("./static/", "./docs/")

    generate_pages_recursive("./content/", "./template.html", "./docs/", basepath)

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