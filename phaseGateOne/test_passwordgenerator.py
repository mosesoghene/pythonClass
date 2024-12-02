from unittest import TestCase
from passwordgenerator import *

class TestPasswordGenerator(TestCase):
    def test_function_exist(self):
        password_generator()
    
    def test_len_of_pass_is_16(self):
        actual = len(password_generator())
        expected = 16
        self.assertEqual(actual, expected)
