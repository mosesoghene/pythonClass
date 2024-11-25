from kata import *
from unittest import TestCase

class TestMaxNumberFunction(TestCase):
    def test_that_function_exists(self):
        max_number([1,2,3])
    
    def test_that_function_returns_correct_result(self):
        actual = max_number([1,2,3,5,4])
        expected = 5
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_empty_list(self):
        self.assertRaises(IndexError, max_number, [])
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, max_number)


class TestReverseArrayFunction(TestCase):
    def test_that_function_exists(self):
        reverse_list([1,2,3])
    
    def test_that_function_returns_correct_result(self):
        actual = reverse_list([1,2,3,5,4])
        expected = [4,5,3,2,1]
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_empty_list(self):
        self.assertRaises(IndexError, reverse_list, [])
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, reverse_list)

class TestValueInFunction(TestCase):
    def test_that_function_exists(self):
        value_in(3, [1,2,3])
    
    def test_that_function_returns_correct_result(self):
        actual = value_in(3, [1,2,3,5,4])
        expected = True
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_empty_list(self):
        self.assertRaises(IndexError, value_in, 3, [])
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, value_in)


class TestGetOddElementsFunction(TestCase):
    def test_that_function_exists(self):
        get_odd_elements([1,2,3,4,5])
    
    def test_that_function_returns_correct_result(self):
        actual = get_odd_elements([1,2,3,4,5])
        expected = [1,3,5]
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_empty_list(self):
        self.assertRaises(IndexError, get_odd_elements, [])
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, get_odd_elements)


class TestGetEvenElementsFunction(TestCase):
    def test_that_function_exists(self):
        get_even_elements([1,2,3,4,5])
    
    def test_that_function_returns_correct_result(self):
        actual = get_even_elements([1,2,3,4,5])
        expected = [2,4]
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_empty_list(self):
        self.assertRaises(IndexError, get_even_elements, [])
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, get_even_elements)


class TestGetRunningSumFunction(TestCase):
    def test_that_function_exists(self):
        get_running_sum([1,2,3,4,5])
    
    def test_that_function_returns_correct_result(self):
        actual = get_running_sum([1,2,3,4,5])
        expected = 15
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_empty_list(self):
        self.assertRaises(IndexError, get_running_sum, [])
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, get_running_sum)


class TestGetIsPalindromeFunction(TestCase):
    def test_that_function_exists(self):
        is_palindrome("eme")
    
    def test_that_function_returns_correct_result(self):
        actual = is_palindrome("eme")
        expected = True
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_empty_str(self):
        self.assertRaises(IndexError, is_palindrome, '')
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, is_palindrome)
        
        
class TestGetJoinListFunction(TestCase):
    def test_that_function_exists(self):
        join_list(["a", "b", "c"],[1,2,3])
    
    def test_that_function_returns_correct_result(self):
        actual = join_list(["a", "b", "c"],[1,2,3])
        expected = ["a", "b", "c", 1, 2, 3]
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_wrong_type_str(self):
        self.assertRaises(TypeError, join_list, '', 4)
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, join_list)


class TestAlternateListFunction(TestCase):
    def test_that_function_exists(self):
        alternate_list(["a", "b", "c"],[1,2,3])
    
    def test_that_function_returns_correct_result(self):
        actual = alternate_list(["a", "b", "c"],[1,2,3])
        expected = ["a", 1, "b", 2, "c", 3]
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_wrong_type_str(self):
        self.assertRaises(TypeError, alternate_list, '', 4)
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, alternate_list)


class TestGetListOfFunction(TestCase):
    def test_that_function_exists(self):
        list_of(2345)
    
    def test_that_function_returns_correct_result(self):
        actual = list_of(2345)
        expected = [2,3,4,5]
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_wrong_arg_type(self):
        self.assertRaises(TypeError, list_of, '')
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, list_of)


class TestIsEvenFunction(TestCase):
    def test_that_function_exists(self):
        is_even(2345)
    
    def test_that_function_returns_correct_result(self):
        actual = is_even(2345)
        expected = False
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_wrong_arg_type(self):
        self.assertRaises(TypeError, is_even, '')
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, is_even)


class TestSubtractFunction(TestCase):
    def test_that_function_exists(self):
        subtract(3,7)
    
    def test_that_function_returns_correct_result(self):
        actual = subtract(3, 7)
        expected = 4
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_wrong_arg_type(self):
        self.assertRaises(TypeError, subtract, '')
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, subtract)


class TestDivideFunction(TestCase):
    def test_that_function_exists(self):
        divide(3,7)
    
    def test_that_function_returns_correct_result(self):
        actual = divide(3, 0)
        expected = 0
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_wrong_arg_type(self):
        self.assertRaises(TypeError, divide, '')
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, divide)


class TestFactorOfFunction(TestCase):
    def test_that_function_exists(self):
        factor_of(10)
    
    def test_that_function_returns_correct_result(self):
        actual = factor_of(10)
        expected = 4
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_wrong_arg_type(self):
        self.assertRaises(TypeError, factor_of, '')
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, factor_of)


class TestIsSquareFunction(TestCase):
    def test_that_function_exists(self):
        is_square(25)
    
    def test_that_function_returns_correct_result(self):
        actual = is_square(25)
        expected = True
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_wrong_arg_type(self):
        self.assertRaises(TypeError, is_square, '')
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, is_square)
        

class TestIsPlaindromeFunction(TestCase):
    def test_that_function_exists(self):
        is_int_palindrome(54145)
    
    def test_that_function_returns_correct_result(self):
        actual = is_int_palindrome(54145)
        expected = True
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_wrong_arg_type(self):
        self.assertRaises(TypeError, is_int_palindrome, '')
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, is_int_palindrome)


class TestFactorialOfFunction(TestCase):
    def test_that_function_exists(self):
        factorial_of(5)
    
    def test_that_function_returns_correct_result(self):
        actual = factorial_of(5)
        expected = 120
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_wrong_arg_type(self):
        self.assertRaises(TypeError, factorial_of, '')
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, factorial_of)
        
        
class TestSquareOfFunction(TestCase):
    def test_that_function_exists(self):
        square_of(5)
    
    def test_that_function_returns_correct_result(self):
        actual = square_of(5)
        expected = 25
        self.assertEqual(actual, expected)
    
    def test_that_fucntion_raises_error_wrong_arg_type(self):
        self.assertRaises(TypeError, square_of, '')
    
    def test_that_function_raises_error_no_argument(self):
        self.assertRaises(TypeError, square_of)
