
import unittest
from unittest.mock import patch
from my_package.hello_world2 import hello


class TestHelloFunction(unittest.TestCase):
    @patch('builtins.print')  # Mock the print function
    def test_hello(self, mock_print):
        hello()  # Call the hello function
        mock_print.assert_called_once_with('hello-world.py')  # Assert print was called with the correct argument
