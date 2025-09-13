import re

def extract_markdown_images(text):

    imgs = re.findall(r"\[(.*?)\]\((.*?\/\/.*?\..*?\))")

    return imgs

def extract_makdown_links(links):

    alt_text_urls = re.findall(r"!\[(.*?)\]\((.*?\/\/.*?\..*?\))")

    return alt_text_urls