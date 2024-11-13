from unittest import TestCase
from flakes import *

class TestDivideOrSquare(TestCase):
    def test_that_function_exists(self):
        divide_or_square(5)

    def test_that_function_returns_correct_number_sqaured(self):
        actual = divide_or_square(10)
        expected = 3.16
        self.assertEqual(actual, expected)
    
    def test_that_function_returns_number_remainder(self):
        actual = divide_or_square(6)
        expected = 1
        self.assertEqual(actual, expected)
    
    def test_that_function_returns_error_for_non_integer_numbers(self):        
        self.assertRaises(TypeError, divide_or_square, 6.0)
    
    def test_that_function_returns_error_for_non_integer_string(self):        
        self.assertRaises(TypeError, divide_or_square, "Hello")
    
    def test_that_function_returns_error_for_float_string(self):        
        self.assertRaises(TypeError, divide_or_square, "10.0")
    
    def test_that_function_returns_correct_value_for_integer_string(self):        
        actual = divide_or_square("10")
        expected = 3.16
        self.assertEqual(actual, expected)
    
    def test_that_function_returns_error_for_no_argument(self):        
        self.assertRaises(TypeError, divide_or_square)
        
        
        

class TestFutureInvestment(TestCase):
    def test_that_function_exists(self):
        get_future_inv(1000, 0.41, 1)

    def test_that_function_returns_correct_value(self):
        actual = get_future_inv(1000, 0.41, 1)
        expected = 1050.32
        self.assertEqual(actual, expected)
    
    def test_that_function_returns_error_for_float_year(self):        
        self.assertRaises(TypeError, get_future_inv, 1000, 0.41, 1.0)    
    
    def test_that_function_returns_error_for_non_integer_string(self):        
        self.assertRaises(TypeError, get_future_inv, "Hello")
    
    def test_that_function_returns_correct_value_for_float_string(self):        
        actual = get_future_inv("1000", "0.41", 1)
        expected = 1050.32
        self.assertEqual(actual, expected)
    
    def test_that_function_returns_correct_value_for_integer_string(self):        
        actual = get_future_inv("1000", 0.41, "1")
        expected = 1050.32
        self.assertEqual(actual, expected)
    
    def test_that_function_returns_error_for_no_argument(self):        
        self.assertRaises(TypeError, get_future_inv)
    

class TestOnlyFloats(TestCase):
    def test_that_function_exists(self):
        only_floats(12.1, 23)
    
    def test_that_function_returns_correct_value_for_one_float(self):
        actual = only_floats(12.1, 23)
        expected = 1
        self.assertEqual(actual, expected)
        
    def test_that_function_returns_correct_value_for_two_floats(self):
        actual = only_floats(12.1, 23.2)
        expected = 2
        self.assertEqual(actual, expected)
    
    def test_that_function_returns_correct_value_for_no_floats(self):
        actual = only_floats(12, 23)
        expected = 0
        self.assertEqual(actual, expected)
    
    def test_that_function_returns_correct_value_for_valid_string_inputs(self):
        actual = only_floats("12.1", "23.2")
        expected = 2
        self.assertEqual(actual, expected)
    
    def test_that_function_returns_correct_value_non_valid_inputs(self):
        self.assertRaises(TypeError, get_future_inv, "idhh")
    
    def test_that_function_returns_correct_value_no_argument_input(self):
        self.assertRaises(TypeError, get_future_inv)
    
    
class TestMyDiscount(TestCase):
    def test_that_function_exists(self):
        my_discount(1000, 10)
    
    def test_that_function_returns_correct_result(self):
        actual = my_discount(150, 15)
        expected = 127.5
        self.assertEqual(actual, expected)
    
    def test_that_function_returns_correct_value_no_argument_input(self):
        self.assertRaises(TypeError, my_discount)
    
    def test_that_function_returns_correct_value_one_argument_input(self):
        self.assertRaises(TypeError, my_discount, 150)
    
    def test_that_function_returns_error_for_invalid_argument_input(self):
        self.assertRaises(TypeError, my_discount, "jhf")
    
    def test_that_function_returns_error_for_negative_argument_input(self):
        self.assertRaises(TypeError, my_discount, -150, 15)
    
    def test_that_function_returns_correct_value_for_one_valid_string_argument_input(self):
        actual = my_discount("150", 15)
        expected = 127.5
        self.assertEqual(actual, expected)
    
    def test_that_function_returns_correct_value_for_two_valid_string_argument_input(self):
        actual = my_discount("150", "15")
        expected = 127.5
        self.assertEqual(actual, expected)
        
