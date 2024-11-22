from unittest import TestCase
from multiplication import multiplication

class TestMultiplicationFunction(TestCase):
    def test_that_multiplication_function_exists(self):
        multiplication(2, 2)
    
    def test_that_multiplication_function_returns_correct_value(self):
        actual = multiplication(2, 2)
        expected = 4
        self.assertEqual(actual, expected)
    
    
    
    def test_that_multiplication_function_raises_exception_with_one_invalid_value(self):        
        self.assertRaises(TypeError, multiplication, "m", 5)
        self.assertRaises(TypeError, multiplication, 2, "o")
        
    def test_that_multiplication_function_raises_exception_with_two_invalid_value(self):
        self.assertRaises(TypeError, multiplication, "s", "e")
    
    def test_that_multiplication_function_raises_exception_with_no_arguments(self):
        self.assertRaises(TypeError, multiplication)
    
    def test_that_multiplication_function_raises_exception_with_less_than_two_arguments(self):
        self.assertRaises(TypeError, multiplication, 5)
    
    def test_that_multiplication_function_raises_exception_with_more_than_two_arguments(self):
        self.assertRaises(TypeError, multiplication, 2, 2, 5)
    
    
    def test_that_multiplication_function_returns_correct_value_for_numbers_in_string_type(self):
        actual = multiplication("2", 2)
        expected = 4
        self.assertEqual(actual, expected)
        
    def test_that_multiplication_function_returns_correct_value_for_two_negative_numbers(self):
        actual = multiplication(-2, -2)
        expected = 4
        self.assertEqual(actual, expected)
        
        actual = multiplication(-2, -2.2)
        expected = 4
        self.assertEqual(actual, expected)
        
        actual = multiplication(-2.2, -2)
        expected = 4
        self.assertEqual(actual, expected)
    
    def test_that_multiplication_function_returns_correct_value_for_one_negative_numbers(self):
        actual = multiplication(-2, 2)
        expected = -4
        self.assertEqual(actual, expected)
        actual = multiplication(2, -2)
        expected = -4
        self.assertEqual(actual, expected)
    
    
    def test_that_multiplication_function_returns_correct_value_for_float_inputs(self):
        actual = multiplication(2.3, 2)
        expected = 5
        self.assertEqual(actual, expected)
