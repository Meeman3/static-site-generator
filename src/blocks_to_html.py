from src.blocks_md import markdown_to_blocks, block_to_block_type, BlockType
from src.htmlnode import HTMLNode
from src.textnode import text_node_to_html_node
from src.inline_md_funcs import text_to_textnodes
import re


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    nodes = []

    for block in markdown_blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEAD:
            if block.startswith("# "):
                heading_txt = block.lstrip("# ")
                nodes.append(HTMLNode(tag= "h1", children= text_to_children(heading_txt)))
            elif block.startswith("## "):
                heading_txt = block.lstrip("## ")
                nodes.append(HTMLNode(tag= "h2", children= text_to_children(heading_txt)))
            elif block.startswith("### "):
                heading_txt = block.lstrip("### ")
                nodes.append(HTMLNode(tag= "h3", children= text_to_children(heading_txt)))
            elif block.startswith("#### "):
                heading_txt = block.lstrip("#### ")
                nodes.append(HTMLNode(tag= "h4", children= text_to_children(heading_txt)))
            elif block.startswith("##### "):
                heading_txt = block.lstrip("##### ")
                nodes.append(HTMLNode(tag= "h5", children= text_to_children(heading_txt)))
            elif block.startswith("###### "):
                heading_txt = block.lstrip("###### ")
                nodes.append(HTMLNode(tag= "h6", children= text_to_children(heading_txt)))

        if block_type == BlockType.CODE:
            nodes.append(HTMLNode(tag= "pre",
                                   children=[HTMLNode(tag= "code", value= block.strip("```"))]))
        
        if block_type == BlockType.QUOTE:
            lines = block.split("\n")
            quote_txt = ""

            for line in lines:
                new_line = line.lstrip("> ")
                quote_txt += new_line

                if lines[-1] != line:
                    quote_txt += "\n"
            
            nodes.append(HTMLNode(tag= "blockquote",
                                   children=[HTMLNode(tag= "p", children = text_to_children(quote_txt))]))

        if block_type == BlockType.UNORD_LIST:
            lines = block.split("\n")
            list_nodes = []
            for line in lines:
                new_line = line.lstrip("- ")
                list_nodes.append(HTMLNode(tag= "li", children= text_to_children(new_line)))

            nodes.append(HTMLNode(tag= "ul", children=list_nodes))
        
        if block_type == BlockType.ORD_LIST:
            lines = block.split("\n")
            list_nodes = []
            for line in lines:
                new_line = re.sub(r"^\d+\. ", "", line)
                list_nodes.append(HTMLNode(tag= "li", children= text_to_children(new_line)))

            nodes.append(HTMLNode(tag= "ol", children=list_nodes))
        
        if block_type == BlockType.PARA:
            
            nodes.append(HTMLNode(tag= "p", children= text_to_children(block)))
        
    Full_HTML_Node = HTMLNode(tag = "div", children=nodes)

    return Full_HTML_Node

def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)

    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    
    return children
    

