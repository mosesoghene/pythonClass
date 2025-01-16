from unittest import TestCase
from searcharray import search_array, count_positive_negative_of


class TestSearch(TestCase):
    def test_search_array_exists(self):
        search_array([], 12)

    def test_search_array_target_not_found(self):
        actual = search_array([12, 17, 24, 32, 14], 0)
        exepected = "Not Available"
        self.assertEqual(actual, exepected)

    def test_search_array_target_found(self):
        actual = search_array([12, 17, 24, 32, 14], 32)
        expected = 3
        self.assertEqual(actual, expected)


class TestCount(TestCase):
    def test_count_positive_negative_of_funcion_exist(self):
        count_positive_negative_of([12, -17, 24, 32, -14])

    def test_count_positive_negative_of_function_returns_correct_result(self):
        actual = count_positive_negative_of([12, -17, 24, 32, -14])
        expected = (3,2, 0)
        self.assertEqual(actual, expected)

    def test_count_positive_negative_of_function_returns_correct_result_with_zeros(self):
        actual = count_positive_negative_of([12, -17, 24, 32, -14, 0])
        expected = (3, 2, 1)


