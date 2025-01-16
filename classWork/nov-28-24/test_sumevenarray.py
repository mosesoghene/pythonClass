from unittest import TestCase
from sumevenarray import *

class TestEvens(TestCase):
    def test_that_correct_result_retruned(self):
        actual = sum_even_of([1,2,3,4,5,6,100])
        expected = 112
        self.assertEquals(actual, expected)        
        
    def test_that_correct_result_retruned(self):
        actual = sum_odds_of([1,2,3,4,5,6,100])
        expected = 9
        self.assertEquals(actual, expected)        
        

class TestOdds(TestCase):     
        
    def test_that_correct_result_retruned(self):
        actual = sum_odds_of([1,2,3,4,5,6,100])
        expected = 9
        self.assertEquals(actual, expected) 


class TestPrimesOf(TestCase):
    def test_that_correct_result_retruned(self):
        actual = get_primes_of(20)
        expected = [2,3,5,7,11,13,17,19]
        self.assertEquals(actual, expected) 
        

class TestArrayEvenCount(TestCase):
    def test_that_function_exist(self):
        count_even([1,5,7,3,2,7,8,10])        
        
    def test_that_correct_result_retruned(self):
        actual = count_even([1,5,7,3,2,7,8,10])
        expected = 3
        self.assertEquals(actual, expected) 
    
    def test_that_correct_result_retruned(self):
        self.assertRaises(TypeError, count_even, "289") 


class TestArrayEvenTrueFalse(TestCase):
    def test_that_function_exist(self):
        true_false_even_odds([1,5,7,3,2,7,8,10])        
        
    def test_that_correct_result_retruned(self):
        actual = true_false_even_odds([1,2,3,4,5,6])
        expected = [False, True, False, True, False, True]
        self.assertEquals(actual, expected) 
    
    def test_that_correct_result_retruned(self):
        self.assertRaises(TypeError, count_even, "289") 


class TestCapitalizeArray(TestCase):
    def test_that_function_exist(self):
        capitalize_(['hello', 'world', 'echo'])        
        
    def test_that_correct_result_retruned(self):
        actual = capitalize_(['hello', 'world', 'echo'])
        expected = ['Hello', 'World', 'Echo']
        self.assertEquals(actual, expected) 
    
    def test_that_correct_result_retruned(self):
        self.assertRaises(TypeError, count_even, "289") 


class TestFunc_(TestCase):
    def test_that_function_exist(self):
        func_()        
        
    def test_that_correct_result_retruned(self):
        actual = func_()
        expected = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
        self.assertEquals(actual, expected) 

class TestSquareOdds(TestCase):
    def test_that_function_exist(self):
        square_odds([3, 6, 9, 12, 15, 18, 21, 24, 27, 30])        
        
    def test_that_correct_result_retruned(self):
        actual = square_odds([3, 6, 9, 12, 15, 18, 21, 24, 27, 30])   
        expected = [9, 81, 225, 441, 729]
        self.assertEquals(actual, expected) 


class TestSquares(TestCase):
    def test_that_function_exist(self):
        squares(4)        
        
    def test_that_correct_result_retruned(self):
        actual = squares(4)   
        expected = [1,4,9,16]
        self.assertEquals(actual, expected) 


class TestAllGreaterThanTen(TestCase):
    def test_that_function_exist(self):
        all_greater_than_ten([1,5,12,15,8])     
    
    def test_that_correct_result_returned(self):
        actual = all_greater_than_ten([1,5,12,15,8])
        expected = [12,15]
        self.assertEquals(actual, expected) 
        

class TestAllIsPalindrome(TestCase):
    def test_that_function_exist(self):
        is_list_palindrome(['madam', 'apple', 'racecar'])     
    
    def test_that_correct_result_returned(self):
        actual = is_list_palindrome(['madam', 'apple', 'racecar'])
        expected = [True, False, True]
        self.assertEquals(actual, expected) 


class TestPayEven(TestCase):
    def test_that_function_exist(self):
        pay_even_dict(10)     
    
    def test_that_correct_result_returned(self):
        actual = pay_even_dict(10)
        expected = {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
        self.assertEquals(actual, expected) 


