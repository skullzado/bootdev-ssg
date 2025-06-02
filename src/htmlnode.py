class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props_str = ""
        for key, value in self.props.items():
            if type(value) is dict:
                inner_dict = 'style="'
                for i_key, i_value in value.items():
                    inner_dict += f"{i_key}: {i_value}; "
                props_str += inner_dict[:-2].strip() + '"'
            else:
                props_str += f'{key}="{value}" '
        return props_str.strip()

    def __repr__(self):
        print("tag=", self.tag)
        print("value=", self.value)
        print("children=", self.children)
        for key, value in self.props.items():
            print(f'{key}="{value}"')
