from src.blocks_to_html import markdown_to_html_node
import os
import re

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.lstrip().startswith("# "):
            return line.strip().lstrip("# ")
        
    raise Exception("No Title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as fp:
        md = fp.read()

    with open(template_path) as temp:
        template = temp.read()

    html_node = markdown_to_html_node(md)
    html = html_node.to_html()

    title = extract_title(md)

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    
    with open(dest_path, "w") as dest:
        dest.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    os.makedirs(dest_dir_path, exist_ok = True)

    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(entry_path) and entry.endswith(".md"):
            file_html  = re.sub(".md", ".html", entry)
            dest_path = os.path.join(dest_dir_path, file_html)
            generate_page(entry_path, template_path, dest_path)

        elif os.path.isdir(entry_path):
            dest_path = os.path.join(dest_dir_path, entry)
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(entry_path, template_path, dest_path)

