from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url):
        super().__init__()
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        self_props = sorted(dir(self))
        other_props = sorted(dir(self))
        if len(self_props) != len(other_props):
            return False
        for i in range(len(self_props)):
            if self_props[i] != other_props[i]:
                return False

        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
