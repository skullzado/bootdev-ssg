import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        matches = extract_markdown_images(old_node.text)

        if not matches:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text

        for i in range(len(matches)):
            text, link = matches[i][0], matches[i][1]
            split_sections = sections.split(f"[{text}]({link})", 1)

            if split_sections[0].strip() == "" and split_sections[1].strip() == "":
                split_nodes.append(TextNode(text, TextType.IMAGE, link))
            elif split_sections[0].strip() == "" or split_sections[0].strip() == "!":
                split_nodes.append(TextNode(text, TextType.IMAGE, link))
            else:
                split_nodes.append(TextNode(split_sections[0][:-1], TextType.TEXT))
                split_nodes.append(TextNode(text, TextType.IMAGE, link))

            sections = split_sections[1]

        new_nodes.extend(split_nodes)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        matches = extract_markdown_links(old_node.text)

        if not matches:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text

        for i in range(len(matches)):
            image_alt, image_link = matches[i][0], matches[i][1]
            split_sections = sections.split(f"[{image_alt}]({image_link})", 1)

            if split_sections[0].strip() == "" and split_sections[1].strip() == "":
                split_nodes.append(TextNode(image_alt, TextType.LINK, image_link))
            elif split_sections[0].strip() == "":
                split_nodes.append(TextNode(image_alt, TextType.LINK, image_link))
            else:
                split_nodes.append(TextNode(split_sections[0], TextType.TEXT))
                split_nodes.append(TextNode(image_alt, TextType.LINK, image_link))

            sections = split_sections[1]

        new_nodes.extend(split_nodes)

    return new_nodes
