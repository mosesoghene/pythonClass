from classwork import *
from unittest import TestCase

class TestGetSwitchedListfunction(TestCase):
    def test_that_function_exists(self):
        get_switched_list([1,2,3,4,5], 2)
    
    def test_that_error_raised_for_no_array_arg(self):
        self.assertRaises(TypeError, get_switched_list, "", 3)
    
    def test_that_error_raised_for_no_int_arg(self):
        self.assertRaises(TypeError, get_switched_list, [1,2,3,4,5], "")
    
    def test_that_correct_result_returned(self):
        actual = get_switched_list([1,2,3,4,5], 2)
        expected = [3, 4, 5, 1, 2]
        self.assertEqual(actual, expected)
    

class TestGetSplitListfunction(TestCase):
    def test_that_function_exists(self):
        get_split_list([1,2,3,4,5])
    
    def test_that_error_raised_for_no_array_arg(self):
        self.assertRaises(TypeError, get_split_list, "")
    
    def test_that_error_raised_for_no_list_arg(self):
        self.assertRaises(TypeError, get_split_list, "")
    
    def test_that_correct_result_returned(self):
        actual = get_split_list([1,2,3,4,5])
        expected = [[1, 2, 3], [4, 5]]
        self.assertEqual(actual, expected)
    

class TestGetEvenOddsfunction(TestCase):
    def test_that_function_exists(self):
        get_even_odds([1,2,3,4,5])
    
    def test_that_error_raised_for_empty_array_arg(self):
        self.assertRaises(IndexError, get_even_odds, [])
    
    def test_that_error_raised_for_no_list_arg(self):
        self.assertRaises(TypeError, get_even_odds, "")
    
    def test_that_correct_result_returned(self):
        actual = get_even_odds([1,2,3,4,5])
        expected = [False, True, False, True, False]
        self.assertEqual(actual, expected)
