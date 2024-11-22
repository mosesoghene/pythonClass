from unittest import TestCase
import functionpractice

class TestCubeFunction(TestCase):
    def test_that_cube_function_exists(self):
        functionpractice.get_cube(3)
    
    def test_that_cube_function_returns_correct_value(self):
        actual = functionpractice.get_cube(3)
        expected = 27
        self.assertEqual(actual, expected)
        
    def test_that_cube_function_raise_exception_with_invalid_input(self):
        self.assertRaises(TypeError, functionpractice.get_cube, "moses")
        
    
    def test_that_cube_function_returns_correct_value_with_float(self):
        actual = functionpractice.get_cube(2.3)
        expected = 12.167
        self.assertEqual(actual, expected)
    
    
    
    
