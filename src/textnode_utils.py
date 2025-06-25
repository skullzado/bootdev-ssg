from textnode import TextType, TextNode, LeafNode


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        nodes = []
        if node.text_type is not TextType.TEXT:
            nodes.append(node)
        else:
            split_text = node.text.split(" ")

            if len(split_text) == 1:
                text = node.text
                if delimiter == "**":
                    nodes.append(TextNode(text[2:-2], text_type))
                else:
                    nodes.append(TextNode(text[1:-1], text_type))
            else:
                is_valid_markdown = [False, False]
                text_so_far = ""
                for text in split_text:
                    if text == delimiter or text == "":
                        continue
                    if text.startswith(delimiter) and text.endswith(delimiter):
                        is_valid_markdown = [True, True]
                        if len(text_so_far):
                            nodes.append(TextNode(text_so_far, TextType.TEXT))
                        text_so_far = " "
                        if delimiter == "**":
                            nodes.append(TextNode(text[2:-2], text_type))
                        else:
                            nodes.append(TextNode(text[1:-1], text_type))
                    elif text.startswith(delimiter):
                        is_valid_markdown[0] = not is_valid_markdown[0]
                        if len(text_so_far):
                            nodes.append(TextNode(text_so_far, TextType.TEXT))
                            text_so_far = text.replace(delimiter, "") + " "
                        else:
                            text_so_far = text.replace(delimiter, "") + " "
                    elif text.endswith(delimiter):
                        is_valid_markdown[1] = not is_valid_markdown[1]
                        text_so_far += text.replace(delimiter, "")
                        nodes.append(TextNode(text_so_far, text_type))
                        text_so_far = " "
                    else:
                        if text == " ":
                            continue
                        elif text == split_text[-1]:
                            if is_valid_markdown[0] and is_valid_markdown[1]:
                                text_so_far += text
                                nodes.append(TextNode(text_so_far, TextType.TEXT))
                            else:
                                raise Exception("invalid markdown syntax")
                        else:
                            text_so_far += text + " "

        new_nodes.extend(nodes)

    return new_nodes
