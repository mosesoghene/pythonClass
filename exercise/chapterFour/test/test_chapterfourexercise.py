from unittest import TestCase
from secondssincemidnight import seconds_since_midnight
from average import average
from celcioustofahrenheit import celcious_to_fahrenheit_table

class TestSecondsSinceMidnight(TestCase):
    def test_that_function_exists(self):
        seconds_since_midnight(13, 30, 45)
    
    def test_that_function_returns_correct_value(self):
        actual = seconds_since_midnight(13, 30, 45)
        expected = 48645
        self.assertEqual(actual, expected)
    
    
class TestAverage(TestCase):
    def test_that_function_exists(self):
        average(2, 3, 6, 1)
    
    def test_that_function_returns_correct_value(self):
        actual = average(2, 3, 6, 1)
        expected = 3
        self.assertEqual(actual, expected)
        celcious_to_fahrenheit_table()
