import unittest
from src.stackds import Stack

class StackDSTest(unittest.TestCase):
    def setUp(self):
        self.numbers = Stack(int, 5)

    def test_that_size_is_zero_by_default(self):
        actual = self.numbers.size()
        expected = 0
        self.assertEqual(actual, expected)

    def test_that_push_size_increase(self):
        self.assertEqual(self.numbers.size(), 0)

        self.numbers.push(3)
        self.assertEqual(self.numbers.size(), 1)

    def test_push_raises_error_for_invalid_types(self):
        with self.assertRaises(TypeError):
            self.numbers.push("3")

    def test_that_push_raises_error_if_stack_is_full(self):
        self.numbers.push(3)
        self.numbers.push(4)
        self.numbers.push(5)
        self.numbers.push(6)
        self.numbers.push(7)
        with self.assertRaises(ValueError):
            self.numbers.push(8)

    def test_that_stack_is_empty_by_default(self):
        self.assertTrue(self.numbers.is_empty())

    def test_that_pop_decreases_size(self):
        self.assertEqual(self.numbers.size(), 0)

        self.numbers.push(3)
        self.numbers.push(4)
        self.numbers.push(5)

        self.assertEqual(self.numbers.size(), 3)

        self.numbers.pop()
        self.assertEqual(self.numbers.size(), 2)

        self.numbers.pop()
        self.assertEqual(self.numbers.size(), 1)

    def test_pop_returns_last_element(self):
        self.numbers.push(3)
        self.numbers.push(4)
        self.numbers.push(5)

        actual = self.numbers.pop()
        self.assertEqual(actual, 5)

        actual = self.numbers.pop()
        self.assertEqual(actual, 4)

    def test_pop_raises_error_if_stack_is_empty(self):
        self.assertTrue(self.numbers.is_empty())

        with self.assertRaises(IndexError):
            self.numbers.pop()

    def test_peek_returns_last_element(self):
        self.numbers.push(3)
        self.numbers.push(4)
        self.numbers.push(5)

        actual = self.numbers.peek()
        self.assertEqual(actual, 5)

        self.numbers.pop()
        self.assertEqual(self.numbers.size(), 2)

        actual = self.numbers.peek()
        self.assertEqual(actual, 4)

    def test_peek_raises_error_if_stack_is_empty(self):
        self.assertTrue(self.numbers.is_empty())

        with self.assertRaises(IndexError):
            self.numbers.pop()

    def test_peek_does_not_decrease_size(self):
        self.numbers.push(3)
        self.numbers.push(4)
        self.numbers.push(5)
        self.assertEqual(self.numbers.size(), 3)

        actual = self.numbers.peek()
        self.assertEqual(actual, 5)

        self.assertEqual(self.numbers.size(), 3)




