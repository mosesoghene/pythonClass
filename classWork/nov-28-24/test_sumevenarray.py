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
