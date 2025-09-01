import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold_text)
        node2 = TextNode("This is a text node", TextType.bold_text)

        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node5 = TextNode("This is a text node", TextType.bold_text, url= "url")
        node6 = TextNode("This is a text node", TextType.bold_text, url = "url")

        self.assertEqual(node5, node6)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.bold_text)
        node3 = TextNode("woweezowee", TextType.bold_text)


        self.assertNotEqual(node, node3)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.bold_text)
        node4 = TextNode("This is a text node", TextType.italic_text)

        self.assertNotEqual(node, node4)

    def test_not_eq_with_url(self):
        node6 = TextNode("This is a text node", TextType.bold_text, url = "url")
        node7 = TextNode("This is a text node", TextType.images, url = "url")

        self.assertNotEqual(node6, node7)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.bold_text, url = "aaaaaaaa")
        self.assertEqual("TextNode(This is a text node, bold, aaaaaaaa)", repr(node))
    
    def test_repr_none(self):
        node = TextNode("This is a text node", TextType.bold_text)
        self.assertEqual("TextNode(This is a text node, bold, None)", repr(node))


if __name__ == "__main__":
    unittest.main()