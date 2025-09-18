# python
import unittest

from src.blocks_md import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph_default(self):
        self.assertEqual(
            block_to_block_type("Just a simple paragraph."),
            BlockType.PARAGRAPH,
        )

    def test_heading_levels_1_to_6(self):
        for i in range(1, 7):
            self.assertEqual(
                block_to_block_type("#" * i + " Heading"),
                BlockType.HEADING,
            )

    def test_heading_needs_space(self):
        # No space after hashes -> not a heading
        self.assertEqual(
            block_to_block_type("##Not a heading"),
            BlockType.PARAGRAPH,
        )

    def test_code_block_triple_backticks(self):
        text = "```\ncode here\n```"
        self.assertEqual(block_to_block_type(text), BlockType.CODE)

    def test_code_block_requires_both_ends(self):
        self.assertEqual(block_to_block_type("```\nno end"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("no start\n```"), BlockType.PARAGRAPH)

    def test_quote_block_all_lines_gt(self):
        text = "> a\n> b\n> c"
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)

    def test_quote_block_fail_if_any_line_missing_gt(self):
        text = "> a\nb"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_unordered_list_dash_space(self):
        text = "- item 1\n- item 2\n- item 3"
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)

    def test_unordered_list_requires_space(self):
        self.assertEqual(block_to_block_type("-no space"), BlockType.PARAGRAPH)

    def test_ordered_list_number_dot_space_incrementing(self):
        text = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)

    def test_ordered_list_must_start_at_one(self):
        text = "2. first\n3. second"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_ordered_list_must_increment_by_one(self):
        text = "1. first\n3. second"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_ordered_list_requires_space(self):
        self.assertEqual(block_to_block_type("1.first"), BlockType.PARAGRAPH)

    def test_single_line_list_not_ordered_without_number(self):
        self.assertEqual(block_to_block_type("1. only line"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("- only line"), BlockType.UNORDERED_LIST)

    def test_heading_valid_multiple_levels(self):
        md = "# Title\n## Sub"
        self.assertEqual(block_to_block_type(md), BlockType.HEAD)

    def test_heading_invalid_too_many_hashes(self):
        md = "# Good\n####### Too many"
        with self.assertRaises(Exception):
            block_to_block_type(md)

    def test_code_fence_triple_backticks(self):
        md = "```\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_quote_valid(self):
        md = "> one\n> two\n> three"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_quote_allows_blank_lines(self):
        md = "> one\n\n> three"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_quote_invalid_mixed(self):
        md = "> one\nnot quote"
        with self.assertRaises(Exception):
            block_to_block_type(md)

    def test_unordered_list_valid(self):
        md = "- a\n- b\n- c"
        self.assertEqual(block_to_block_type(md), BlockType.UNORD_LIST)

    def test_unordered_list_allows_blank_lines(self):
        md = "- a\n\n- c"
        self.assertEqual(block_to_block_type(md), BlockType.UNORD_LIST)

    def test_unordered_list_invalid_mixed(self):
        md = "- a\nb"
        with self.assertRaises(Exception):
            block_to_block_type(md)

    def test_ordered_list_valid_incrementing(self):
        md = "1. a\n2. b\n3. c"
        self.assertEqual(block_to_block_type(md), BlockType.ORD_LIST)

    def test_ordered_list_allows_blank_lines(self):
        md = "1. a\n\n2. b"
        self.assertEqual(block_to_block_type(md), BlockType.ORD_LIST)

    def test_ordered_list_invalid_jump(self):
        md = "1. a\n3. c"
        with self.assertRaises(Exception):
            block_to_block_type(md)

    def test_paragraph_fallback(self):
        md = "just a paragraph\nwith two lines"
        self.assertEqual(block_to_block_type(md), BlockType.PARA)

if __name__ == "__main__":
    unittest.main()