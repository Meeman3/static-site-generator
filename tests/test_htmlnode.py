import unittest
from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_props(self):
        node = HTMLNode(props={"href": "abc", "target": "def"})
        self.assertEqual(' href="abc" target="def"', node.props_to_html())

    def test_init_values(self):
        node = HTMLNode("tag", "insert text here", [1, 2])

        self.assertEqual(node.tag, "tag")
        self.assertEqual(node.value, "insert text here")
        self.assertEqual(node.children, [1, 2])
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("tag", "insert text here", [1, 2], {"href": "abc", "target": "def"})

        self.assertEqual(repr(node), "HTMLNode(tag, insert text here, [1, 2], {'href': 'abc', 'target': 'def'})")


