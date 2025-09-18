
import os
import shutil


def main():

    dir_copy("./static/", "./public/")

def dir_copy(src_dir, dst_dir):
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
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