import unittest

from src.textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node5 = TextNode("This is a text node", TextType.BOLD, url= "url")
        node6 = TextNode("This is a text node", TextType.BOLD, url = "url")

        self.assertEqual(node5, node6)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("woweezowee", TextType.BOLD)


        self.assertNotEqual(node, node3)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.ITALIC)

        self.assertNotEqual(node, node4)

    def test_not_eq_with_url(self):
        node6 = TextNode("This is a text node", TextType.BOLD, url = "url")
        node7 = TextNode("This is a text node", TextType.ITALIC, url = "url")

        self.assertNotEqual(node6, node7)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, url = "aaaaaaaa")
        self.assertEqual("TextNode(This is a text node, bold, aaaaaaaa)", repr(node))
    
    def test_repr_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual("TextNode(This is a text node, bold, None)", repr(node))

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_except(self):
        with self.assertRaises(Exception):
            text_node_to_html_node(TextNode("This is error", TextType.wowee))


if __name__ == "__main__":
    unittest.main()