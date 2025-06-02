import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        link_htmlnode = HTMLNode(
            "a",
            "This is an Anchor tage",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        heading_htmlnode = HTMLNode(
            "h1", "This is an heading tag", None, {"id": "heading", "class": "heading"}
        )
        div_htmlnode = HTMLNode(
            "img",
            "This is HTML div tag",
            None,
            {"id": "main", "style": {"width": "240px", "height": "120px"}},
        )

        self.assertEqual(
            link_htmlnode.props_to_html(),
            'href="https://www.google.com" target="_blank"',
        )

        self.assertEqual(
            heading_htmlnode.props_to_html(), 'id="heading" class="heading"'
        )

        self.assertEqual(
            div_htmlnode.props_to_html(),
            'id="main" style="width: 240px; height: 120px"',
        )
