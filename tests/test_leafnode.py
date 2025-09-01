import unittest

from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_init(self):
        node = LeafNode("p", "text here", {"a": "b", "c": "d"})
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, 'text here')
        self.assertEqual(node.props, {'a': 'b', 'c': 'd'})
        self.assertEqual(node.children, None)
    
    def test_leaf_to_html_edge(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()

        node2 = LeafNode(None, "Hello, world!")
        self.assertEqual(node2.to_html(), 'Hello, world!')

    def test_leaf_repr(self):
        node = LeafNode("p", "text", {"a": "b", "c": "d"})
        self.assertEqual(repr(node), "LeafNode(p, text, {'a': 'b', 'c': 'd'})")
