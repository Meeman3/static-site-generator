import unittest
from src.blocks_to_html import markdown_to_html_node, text_to_children 

class TestMarkdownToHTML(unittest.TestCase):
    
    def test_simple_paragraph(self):
        markdown = "This is a simple paragraph"
        result = markdown_to_html_node(markdown)
        
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 1)
        self.assertEqual(result.children[0].tag, "p")
        self.assertEqual(result.children[0].children[0].value, "This is a simple paragraph")
    
    def test_simple_header(self):
        markdown = "# Hello World"
        result = markdown_to_html_node(markdown)
        
        self.assertEqual(result.tag, "div")
        self.assertEqual(result.children[0].tag, "h1")
        self.assertEqual(result.children[0].children[0].value, "Hello World")
    
    def test_header_with_bold(self):
        markdown = "# Hello **World**"
        result = markdown_to_html_node(markdown)
        
        self.assertEqual(result.tag, "div")
        self.assertEqual(result.children[0].tag, "h1")

        self.assertTrue(len(result.children[0].children) >= 2)

        bold_found = any(child.tag == "b" for child in result.children[0].children)
        self.assertTrue(bold_found)
    
    def test_unordered_list(self):
        markdown = "- First\n- Second"
        result = markdown_to_html_node(markdown)
        
        self.assertEqual(result.tag, "div")
        self.assertEqual(result.children[0].tag, "ul")
        self.assertEqual(len(result.children[0].children), 2)
        self.assertEqual(result.children[0].children[0].tag, "li")
        self.assertEqual(result.children[0].children[1].tag, "li")
    
    def test_code_block(self):
        markdown = "```\nhello\n```"
        result = markdown_to_html_node(markdown)
        
        self.assertEqual(result.tag, "div")
        self.assertEqual(result.children[0].tag, "pre")
        self.assertEqual(result.children[0].children[0].tag, "code")

        self.assertIn("hello", result.children[0].children[0].value)
    
    def test_multiple_headers(self):
        markdown = "# Header 1\n\n## Header 2\n\n### Header 3"
        result = markdown_to_html_node(markdown)
        
        self.assertEqual(result.tag, "div")
        self.assertEqual(len(result.children), 3)
        self.assertEqual(result.children[0].tag, "h1")
        self.assertEqual(result.children[1].tag, "h2")
        self.assertEqual(result.children[2].tag, "h3")
        self.assertEqual(result.children[0].children[0].value, "Header 1")
        self.assertEqual(result.children[1].children[0].value, "Header 2")
        self.assertEqual(result.children[2].children[0].value, "Header 3")

def test_ordered_list(self):
    markdown = "1. First item\n2. Second item\n3. Third item"
    result = markdown_to_html_node(markdown)
    
    self.assertEqual(result.tag, "div")
    self.assertEqual(result.children[0].tag, "ol")
    self.assertEqual(len(result.children[0].children), 3)
    self.assertEqual(result.children[0].children[0].tag, "li")
    self.assertEqual(result.children[0].children[1].tag, "li")
    self.assertEqual(result.children[0].children[2].tag, "li")
    self.assertEqual(result.children[0].children[0].children[0].value, "First item")
    self.assertEqual(result.children[0].children[1].children[0].value, "Second item")
    self.assertEqual(result.children[0].children[2].children[0].value, "Third item")

def test_blockquote(self):
    markdown = "> This is a quote\n> with multiple lines"
    result = markdown_to_html_node(markdown)
    
    self.assertEqual(result.tag, "div")
    self.assertEqual(result.children[0].tag, "blockquote")
    self.assertEqual(result.children[0].children[0].tag, "p")

    quote_text = result.children[0].children[0].children[0].value
    self.assertIn("This is a quote", quote_text)
    self.assertIn("with multiple lines", quote_text)

def test_paragraph_with_bold(self):
    markdown = "This is **bold** text"
    result = markdown_to_html_node(markdown)
    
    self.assertEqual(result.tag, "div")
    self.assertEqual(result.children[0].tag, "p")
    self.assertEqual(len(result.children[0].children), 3)
    self.assertEqual(result.children[0].children[0].value, "This is ")
    self.assertEqual(result.children[0].children[1].tag, "b")
    self.assertEqual(result.children[0].children[1].value, "bold")
    self.assertEqual(result.children[0].children[2].value, " text")

def test_paragraph_with_italic(self):
    markdown = "This has _italic_ text"
    result = markdown_to_html_node(markdown)
    
    self.assertEqual(result.tag, "div")
    self.assertEqual(result.children[0].tag, "p")
    self.assertEqual(len(result.children[0].children), 3)
    self.assertEqual(result.children[0].children[0].value, "This has ")
    self.assertEqual(result.children[0].children[1].tag, "i")
    self.assertEqual(result.children[0].children[1].value, "italic")
    self.assertEqual(result.children[0].children[2].value, " text")

def test_paragraph_with_code(self):
    markdown = "This has `code` in it"
    result = markdown_to_html_node(markdown)
    
    self.assertEqual(result.tag, "div")
    self.assertEqual(result.children[0].tag, "p")
    self.assertEqual(len(result.children[0].children), 3)
    self.assertEqual(result.children[0].children[0].value, "This has ")
    self.assertEqual(result.children[0].children[1].tag, "code")
    self.assertEqual(result.children[0].children[1].value, "code")
    self.assertEqual(result.children[0].children[2].value, " in it")

def test_paragraph_with_link(self):
    markdown = "Visit [Boot.dev](https://boot.dev) for learning"
    result = markdown_to_html_node(markdown)
    
    self.assertEqual(result.tag, "div")
    self.assertEqual(result.children[0].tag, "p")
    self.assertEqual(len(result.children[0].children), 3)
    self.assertEqual(result.children[0].children[0].value, "Visit ")
    self.assertEqual(result.children[0].children[1].tag, "a")
    self.assertEqual(result.children[0].children[1].value, "Boot.dev")
    self.assertEqual(result.children[0].children[2].value, " for learning")

def test_list_with_formatting(self):
    markdown = "- Item with **bold**\n- Item with _italic_"
    result = markdown_to_html_node(markdown)
    
    self.assertEqual(result.tag, "div")
    self.assertEqual(result.children[0].tag, "ul")
    self.assertEqual(len(result.children[0].children), 2)
    

    first_li = result.children[0].children[0]
    self.assertEqual(first_li.tag, "li")
    self.assertEqual(len(first_li.children), 2)
    self.assertEqual(first_li.children[1].tag, "b")
    

    second_li = result.children[0].children[1]
    self.assertEqual(second_li.tag, "li")
    self.assertEqual(len(second_li.children), 2)
    self.assertEqual(second_li.children[1].tag, "i")

def test_mixed_content(self):
    markdown = "# Title\n\nThis is a paragraph.\n\n- List item"
    result = markdown_to_html_node(markdown)
    
    self.assertEqual(result.tag, "div")
    self.assertEqual(len(result.children), 3)
    self.assertEqual(result.children[0].tag, "h1")
    self.assertEqual(result.children[1].tag, "p")
    self.assertEqual(result.children[2].tag, "ul")

def test_empty_markdown(self):
    markdown = ""
    result = markdown_to_html_node(markdown)
    
    self.assertEqual(result.tag, "div")
    self.assertEqual(len(result.children), 0)

if __name__ == "__main__":
    unittest.main()
