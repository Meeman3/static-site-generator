from enum import Enum
import re

class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORD_LIST = "unordered_list"
    ORD_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned = []
    for block in blocks:
        if block != "":
            cleaned.append(block.strip())


    return cleaned


def block_to_block_type(md_txt):
    lines = md_txt.split("\n")


    if md_txt.startswith("#"):
        head = True
        for line in lines:
            if re.match(r"^#{1,6} ", line):
                continue
            else:
                head = False
        
        if head == True:
            return BlockType.HEAD
        else:
            raise Exception("invalid heading")

    if md_txt.startswith("```") and md_txt.endswith("```"):
        return BlockType.CODE
    
    if md_txt.startswith(">"):
        quote = True

        for line in lines:
            if line.startswith(">"):
                continue
            else:
                quote = False
        
        if quote == True:
            return BlockType.QUOTE
        else:
            raise Exception("invalid quote")
    
    if md_txt.startswith("- "):
        unord_list = True

        for line in lines:
            if line.startswith("- "):
                continue
            else:
                unord_list = False
        
        if unord_list == True:
            return BlockType.UNORD_LIST
        else:
            raise Exception("invalid unordered list")
    
    
    if md_txt[0].isdigit():
        ord_list = True
        num = 1

        for line in lines:
            if line.startswith(f"{num}. "):
                num += 1
                continue
            else:
                ord_list = False
        
        if ord_list == True:
            return BlockType.ORD_LIST
        else:
            raise Exception("invalid ordered list")
        
    return BlockType.PARA