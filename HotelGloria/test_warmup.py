from unittest import TestCase
from warmup import *


class TestGetEvens(TestCase):
    def test_get_evens(self):
        get_evens("1234567wer7dfg")

    def test_that_function_retruns_correct_results(self):
        actual = get_evens("uygqw weuy3w97tcwg919171ufyfyfhjvtty7guk")
        expected = []
        self.assertEqual(actual, expected)


class TestGetSquares(TestCase):
    def test_get_squares(self):
        get_squares(3)

    def test_that_function_retruns_correct_results(self):
        actual = get_squares(5)
        expected = {1:5, 2:25}
        self.assertEqual(actual, expected)
