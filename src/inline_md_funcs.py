import re
from src.textnode import TextNode, TextType

def extract_markdown_images(text):

    imgs = re.findall(r"!\[(.*?)\]\((.*?)\)", text)

    return imgs

def extract_markdown_links(links):

    alt_text_urls = re.findall(r"\[(.*?)\]\((.*?)\)", links)

    return alt_text_urls

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    if delimiter not in {"**", "_", "`"}:
        raise Exception("invalid markdown syntax")
    
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_node = node.text.split(delimiter)

        if len(split_node) % 2 == 0:
            raise Exception("markdown syntax not closed")
        
        if len(split_node) == 1:
            new_nodes.append(node)
            continue
        
        for i, split in enumerate(split_node):
            if split == "":
                continue
            elif i % 2:
                new_nodes.append(TextNode(f"{split}", text_type))
            else:
                new_nodes.append(TextNode(f"{split}", TextType.TEXT))

    
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        old_text = old_node.text
        imgs = extract_markdown_images(old_text)

        if len(imgs) == 0:
            new_nodes.append(old_node)
            continue

        for img in imgs:
            split_txt = old_text.split(f"![{img[0]}]({img[1]})", 1)

            if len(split_txt) != 2:
                raise ValueError("invalid markdown image")
            
            if split_txt[0] != "":
                new_nodes.append(TextNode(split_txt[0], TextType.TEXT))

            new_nodes.append(
                TextNode(
                f"{img[0]}", TextType.IMAGE, f"{img[1]}"
                )
            )

            old_text = split_txt[1]

        if old_text != "":
            new_nodes.append(TextNode(old_text, TextType.TEXT))
        
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        old_text = old_node.text
        links = extract_markdown_links(old_text)

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for link in links:
            split_txt = old_text.split(f"[{link[0]}]({link[1]})", 1)

            if len(split_txt) != 2:
                raise ValueError("invalid markdown image")
            
            if split_txt[0] != "":
                new_nodes.append(TextNode(split_txt[0], TextType.TEXT))

            new_nodes.append(
                TextNode(
                f"{link[0]}", TextType.LINK, f"{link[1]}"
                )
            )

            old_text = split_txt[1]

        if old_text != "":
            new_nodes.append(TextNode(old_text, TextType.TEXT))
        

    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_image(nodes)

    nodes = split_nodes_link(nodes)

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes