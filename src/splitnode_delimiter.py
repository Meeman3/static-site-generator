from src.textnode import TextNode, TextType

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
        
        for i, split in enumerate(split_node):
            if split == "":
                continue
            elif i % 2:
                new_nodes.append(TextNode(f"{split}", text_type))
            else:
                new_nodes.append(TextNode(f"{split}", TextType.TEXT))

    
    return new_nodes