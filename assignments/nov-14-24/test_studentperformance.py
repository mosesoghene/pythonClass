from unittest import TestCase
from studentperformance import *

class TestGetStudentDataFunction(TestCase):
    def test_that_function_exists(self):
        get_student_data()
    
    def test_that_function_returns_list_typre(self):
        actual = type(get_student_data())
        expected = list
        self.assertEquals(actual, expected)
    
    

