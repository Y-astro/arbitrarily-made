import unittest
from unittest.mock import patch
from search import search  

class TestSearchClass(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["hello world", "world"])
    def test_found(self, mock_input):
        s = search()
        s.input()
        with patch('builtins.print') as mock_print:
            s.position()
            mock_print.assert_called_with("'world' found at position 6")
    
    @patch('builtins.input', side_effect=["hello world", "python"])
    def test_not_found(self, mock_input):
        s = search()
        s.input()
        with patch('builtins.print') as mock_print:
            s.position()
            mock_print.assert_called_with("'python' not found in the main string.")

if __name__ == '__main__':
    unittest.main()
