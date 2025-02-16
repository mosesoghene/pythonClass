import unittest
from src.queueds import Queue

class QueueDSTest(unittest.TestCase):
    def setUp(self):
        self.numbers = Queue(int, 5)

    def test_that_size_is_zero_by_default(self):
        actual = self.numbers.size()
        expected = 0
        self.assertEqual(actual, expected)

    def test_that_enqueue_size_increase(self):
        self.assertEqual(self.numbers.size(), 0)

        self.numbers.enqueue(3)
        self.assertEqual(self.numbers.size(), 1)

    def test_enqueue_raises_error_for_invalid_types(self):
        with self.assertRaises(TypeError):
            self.numbers.enqueue("3")

    def test_that_enqueue_raises_error_if_stack_is_full(self):
        self.numbers.enqueue(3)
        self.numbers.enqueue(4)
        self.numbers.enqueue(5)
        self.numbers.enqueue(6)
        self.numbers.enqueue(7)
        with self.assertRaises(ValueError):
            self.numbers.enqueue(8)

    def test_that_stack_is_empty_by_default(self):
        self.assertTrue(self.numbers.is_empty())

    def test_that_dequeue_decreases_size(self):
        self.assertEqual(self.numbers.size(), 0)

        self.numbers.enqueue(3)
        self.numbers.enqueue(4)
        self.numbers.enqueue(5)

        self.assertEqual(self.numbers.size(), 3)

        self.numbers.dequeue()
        self.assertEqual(self.numbers.size(), 2)

        self.numbers.dequeue()
        self.assertEqual(self.numbers.size(), 1)

    def test_dequeue_returns_last_element(self):
        self.numbers.enqueue(3)
        self.numbers.enqueue(4)
        self.numbers.enqueue(5)

        actual = self.numbers.dequeue()
        self.assertEqual(actual, 3)

        actual = self.numbers.dequeue()
        self.assertEqual(actual, 4)

    def test_dequeue_raises_error_if_stack_is_empty(self):
        self.assertTrue(self.numbers.is_empty())

        with self.assertRaises(IndexError):
            self.numbers.dequeue()

    def test_peek_returns_last_element(self):
        self.numbers.enqueue(3)
        self.numbers.enqueue(4)
        self.numbers.enqueue(5)

        actual = self.numbers.peek()
        self.assertEqual(actual, 3)

        self.numbers.dequeue()
        self.assertEqual(self.numbers.size(), 2)

        actual = self.numbers.peek()
        self.assertEqual(actual, 4)

    def test_peek_raises_error_if_stack_is_empty(self):
        self.assertTrue(self.numbers.is_empty())

        with self.assertRaises(IndexError):
            self.numbers.dequeue()

    def test_peek_does_not_decrease_size(self):
        self.numbers.enqueue(3)
        self.numbers.enqueue(4)
        self.numbers.enqueue(5)
        self.assertEqual(self.numbers.size(), 3)

        actual = self.numbers.peek()
        self.assertEqual(actual, 3)

        self.assertEqual(self.numbers.size(), 3)




