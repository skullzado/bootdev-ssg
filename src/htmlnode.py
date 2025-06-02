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
        if self.props is None:
            return props_str
        for key, value in self.props.items():
            if type(value) is dict:
                inner_dict = 'style="'
                for i_key, i_value in value.items():
                    inner_dict += f"{i_key}: {i_value}; "
                print(inner_dict)
                props_str += inner_dict[:-2].strip() + '"'
            else:
                props_str += f'{key}="{value}" '
        return " " + props_str.rstrip()

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
