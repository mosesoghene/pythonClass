from functions import *
from unittest import TestCase

class TestSumOfEvenFunction(TestCase):
    def test_that_function_exists(self):
        sum_of_even([])
    
    def test_that_a_list_was_passed_to_function(self):
        self.assertRaises(TypeError, sum_of_even, "8")
    
    def test_that_function_returns_correct_result(self):
        actual = sum_of_even([8, 4])
        expected = 12
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, sum_of_even)


class TestVowelCountOfFunction(TestCase):
    def test_that_function_exists(self):
        vowel_count_of("")
    
    def test_that_a_str_was__not_passed_to_function(self):
        self.assertRaises(TypeError, vowel_count_of, [])
        self.assertRaises(TypeError, vowel_count_of, 8)        
        self.assertRaises(TypeError, vowel_count_of, 9.70)
        self.assertRaises(TypeError, vowel_count_of, {4, 5,6,7})
    
    def test_that_function_returns_correct_result(self):
        actual = vowel_count_of("python is sweet")
        expected = 4
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, vowel_count_of)


class TestIsAnagramFunction(TestCase):
    def test_that_function_exists(self):
        is_anagram("silent", "listen")
    
    def test_that_a_str_was_not_passed_to_function(self):
        self.assertRaises(TypeError, is_anagram, [])
        self.assertRaises(TypeError, is_anagram, 8)        
        self.assertRaises(TypeError, is_anagram, 9.70)
        self.assertRaises(TypeError, is_anagram, {4, 5,6,7})
    
    def test_that_function_returns_correct_result(self):
        actual = is_anagram("silent", "listen")
        expected = True
        self.assertEqual(actual, expected)
        actual = is_anagram("silent", "liste")
        expected = False
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, is_anagram)


class TestIsPrimeFunction(TestCase):
    def test_that_function_exists(self):
        is_prime(3)
    
    def test_that_a_int_was_not_passed_to_function(self):
        self.assertRaises(TypeError, is_prime, [])
        self.assertRaises(TypeError, is_prime, {})        
        self.assertRaises(TypeError, is_prime, "87")
    
    def test_that_function_returns_correct_result(self):
        actual = is_prime(7)
        expected = True
        self.assertEqual(actual, expected)
        actual = is_prime(9)
        expected = False
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, is_prime)


class TestIsPalindromeFunction(TestCase):
    def test_that_function_exists(self):
        is_palindrom("madam")
    
    def test_that_a_str_was_not_passed_to_function(self):
        self.assertRaises(TypeError, is_palindrom, [])
        self.assertRaises(TypeError, is_palindrom, {})        
        self.assertRaises(TypeError, is_palindrom, 87)
    
    def test_that_function_returns_correct_result(self):
        actual = is_palindrom("madam")
        expected = True
        self.assertEqual(actual, expected)
        actual = is_palindrom("madman")
        expected = False
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, is_palindrom)


class TestAverageFunction(TestCase):
    def test_that_function_exists(self):
        average([10,20,30,40])
    
    def test_that_a_list_was_not_passed_to_function(self):
        self.assertRaises(TypeError, average, 9)
        self.assertRaises(TypeError, average, {})        
        self.assertRaises(TypeError, average, 87)
    
    def test_that_function_returns_correct_result(self):
        actual = average([10,20,30,40])
        expected = 25.0
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, average)


class TestReverseStringFunction(TestCase):
    def test_that_function_exists(self):
        reverse_string("hello")
    
    def test_that_a_str_was_not_passed_to_function(self):
        self.assertRaises(TypeError, reverse_string, 9)
        self.assertRaises(TypeError, reverse_string, {})        
        self.assertRaises(TypeError, reverse_string, 87)
    
    def test_that_function_returns_correct_result(self):
        actual = reverse_string("hello")
        expected = "olleh"
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, reverse_string)

class TestCapitaliseListFunction(TestCase):
    def test_that_function_exists(self):
        capitalise_list(["hello", "mr", "alfred"])
    
    def test_that_a_list_was_not_passed_to_function(self):
        self.assertRaises(TypeError, capitalise_list, 9)
        self.assertRaises(TypeError, capitalise_list, {})        
        self.assertRaises(TypeError, capitalise_list, 87)
    
    def test_that_function_returns_correct_result(self):
        actual = capitalise_list(["hello", "mr", "alfred"])
        expected = ["Hello", "Mr", "Alfred"]
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, capitalise_list)


class TestContainsDuplicateFunction(TestCase):
    def test_that_function_exists(self):
        contains_duplicate([1,2,3,4,5,6,2])
    
    def test_that_a_list_was_not_passed_to_function(self):
        self.assertRaises(TypeError, contains_duplicate, 9)
        self.assertRaises(TypeError, contains_duplicate, {})        
        self.assertRaises(TypeError, contains_duplicate, 87)
    
    def test_that_function_returns_correct_result(self):
        actual = contains_duplicate([1,2,3,4,5,6,2])
        expected = True
        self.assertEqual(actual, expected)
        actual = contains_duplicate([1,2,3,4,5,6])
        expected = False
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, contains_duplicate)


class TestRemoveSpacesFunction(TestCase):
    def test_that_function_exists(self):
        remove_spaces("Hello Python")
    
    def test_that_a_str_was_not_passed_to_function(self):
        self.assertRaises(TypeError, remove_spaces, 9)
        self.assertRaises(TypeError, remove_spaces, {})        
        self.assertRaises(TypeError, remove_spaces, 87)
    
    def test_that_function_returns_correct_result(self):
        actual = remove_spaces("Hello Python")
        expected = "HelloPython"
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, remove_spaces)

class TestGetIntersectFunction(TestCase):
    def test_that_function_exists(self):
        get_intersect([1,2,3], [3,4,5])
    
    def test_that_a_str_was_not_passed_to_function(self):
        self.assertRaises(TypeError, get_intersect, 9)
        self.assertRaises(TypeError, get_intersect, {})        
        self.assertRaises(TypeError, get_intersect, 87)
    
    def test_that_function_returns_correct_result(self):
        actual = get_intersect([1,2,3], [3,4,5])
        expected = 3
        self.assertEqual(actual, expected)
        actual = get_intersect([1,2,3,3,4], [3,3,4,5])
        expected = [3,4]
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, get_intersect)

class TestSortedByLenOfStringFunction(TestCase):
    def test_that_function_exists(self):
        sorted_by_len_of_string(["apple", "cashews", "cherry"])
    
    def test_that_a_list_was_not_passed_to_function(self):
        self.assertRaises(TypeError, sorted_by_len_of_string, 9)
        self.assertRaises(TypeError, sorted_by_len_of_string, {})        
        self.assertRaises(TypeError, sorted_by_len_of_string, 87)
    
    def test_that_function_returns_correct_result(self):
        actual = sorted_by_len_of_string(["apple", "cashews", "cherry"])
        expected = ["apple", "cherry","cashews"]
        self.assertEqual(actual, expected)
        
        actual = sorted_by_len_of_string(["apple", "cashews", "cherry", "hello"])
        expected = ["apple", "hello", "cherry", "cashews", ]
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, sorted_by_len_of_string)


class TestFactorialFunction(TestCase):
    def test_that_function_exists(self):
        factorial(5)
    
    def test_that_a_int_was_not_passed_to_function(self):
        self.assertRaises(TypeError, factorial, 9.0)
        self.assertRaises(TypeError, factorial, {})        
        self.assertRaises(TypeError, factorial, 87.8)
    
    def test_that_function_returns_correct_result(self):
        actual = factorial(5)
        expected = 120
        self.assertEqual(actual, expected)
        
        actual = factorial(4)
        expected = 24
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, factorial)


class TestFSumOfDigitsFunction(TestCase):
    def test_that_function_exists(self):
        sum_of_digits(15324)
    
    def test_that_a_int_or_str_was_not_passed_to_function(self):
        self.assertRaises(TypeError, sum_of_digits, 9.0)
        self.assertRaises(TypeError, sum_of_digits, {})        
        self.assertRaises(TypeError, sum_of_digits, 87.8)
    
    def test_that_function_returns_correct_result(self):
        actual = sum_of_digits("15324")
        expected = 15
        self.assertEqual(actual, expected)
        
        actual = sum_of_digits(15324)
        expected = 15
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, sum_of_digits)


class TestFSumOfOddDigitsFunction(TestCase):
    def test_that_function_exists(self):
        sum_of_odd_digits(12345)
    
    def test_that_a_int_or_str_was_not_passed_to_function(self):
        self.assertRaises(TypeError, sum_of_odd_digits, 9.0)
        self.assertRaises(TypeError, sum_of_odd_digits, {})        
        self.assertRaises(TypeError, sum_of_odd_digits, 87.8)
    
    def test_that_function_returns_correct_result(self):
        actual = sum_of_odd_digits("15324")
        expected = 9
        self.assertEqual(actual, expected)
        
        actual = sum_of_odd_digits(15324)
        expected = 9
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, sum_of_odd_digits)


       

class TestgetAcronymFunction(TestCase):
    def test_that_function_exists(self):
        get_acronym("Portable Network Graphics")
    
    def test_that_a_str_was_not_passed_to_function(self):
        self.assertRaises(TypeError, get_acronym, 9.0)
        self.assertRaises(TypeError, get_acronym, {})        
        self.assertRaises(TypeError, get_acronym, 87.8)
    
    def test_that_function_returns_correct_result(self):
        actual = get_acronym("Portable Network Graphics")
        expected = "PNG"
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, get_acronym)


class TestSumOfProductFunction(TestCase):
    def test_that_function_exists(self):
        sum_of_product([1,2,3,4])
    
    def test_that_a_str_was_not_passed_to_function(self):
        self.assertRaises(TypeError, sum_of_product, 9.0)
        self.assertRaises(TypeError, sum_of_product, {})        
        self.assertRaises(TypeError, sum_of_product, 87.8)
    
    def test_that_function_returns_correct_result(self):
        actual = sum_of_product([1,2,3,4])
        expected = 30
        self.assertEqual(actual, expected)
        
        actual = sum_of_product([1,2,3,4,5])
        expected = 60
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, sum_of_product)


class TestMergeAndSortFunction(TestCase):
    def test_that_function_exists(self):
        merge_and_sort([1, 3, 5], [2, 4, 6])
    
    def test_that_a_int_or_str_was_not_passed_to_function(self):
        self.assertRaises(TypeError, merge_and_sort, 9.0)
        self.assertRaises(TypeError, merge_and_sort, {})        
        self.assertRaises(TypeError, merge_and_sort, 87.8)
    
    def test_that_function_returns_correct_result(self):
        actual = merge_and_sort([3,4,9,10], [1,5,7,8])
        expected = [1, 3, 4, 5, 7, 8, 9, 10]
        self.assertEqual(actual, expected)
    
    def test_that_function_raises_error_with_no_argument_passed(self):
        self.assertRaises(TypeError, merge_and_sort)
