import unittest
from search import search  

class TestSearch(unittest.TestCase):

    def test_found_case(self):
        s = search("hello world", "world")
        result = s.perform_search()
        self.assertEqual(result, "'world' found at position 6")

    def test_not_found_case(self):
        s = search("hello world", "python")
        result = s.perform_search()
        self.assertEqual(result, "'python' not found in the main string.")

    def test_empty_search_string(self):
        s = search("hello", "")
        result = s.perform_search()
        self.assertEqual(result, "'' found at position 0")  

    def test_empty_main_string(self):
        s = search("", "any")
        result = s.perform_search()
        self.assertEqual(result, "'any' not found in the main string.")

if __name__ == '__main__':
    unittest.main()
