import unittest

from src.stringkata import swapchars, count_of, arrange_word,insert_into, frequency_of, remove_special_chars


class FrequncyCounter(unittest.TestCase):
    def test_function_exists(self):
        frequency_of("semicolon.africa")

    def test_function_returns_correct_value(self):
        actual = frequency_of("semicolon.africa")
        expected = {'s': 1, 'e': 1, 'm': 1, 'i': 2, 'c': 2, 'o': 2, 'l': 1, 'n': 1, '.': 1, 'a': 2, 'f': 1, 'r': 1}
        self.assertEqual(actual, expected)

    def test_function_takes_only_str_type(self):
        with self.assertRaises(TypeError):
            frequency_of([1,2,3,4,6])

    def test_function_doesnt_accept_empty_string(self):
        with self.assertRaises(ValueError):
            frequency_of('')



class SwapChars(unittest.TestCase):
    def test_function_exists(self):
        self.assertTrue(swapchars)

    def test_function_takes_only_string_type(self):
        with self.assertRaises(TypeError):
            swapchars(1)

    def test_function_takes_string_type(self):
        swapchars("abc, xyz")

    def test_function_returns_correct_result(self):
        actual = swapchars("abc, xyz")
        self.assertEqual(actual, "xyc abz")


class TestInsertInto(unittest.TestCase):
    def test_function_exists(self):
        insert_into("helloo", "ce")

    def test_function_takes_only_string_type(self):
        with self.assertRaises(TypeError):
            insert_into("helloo", 2)

    def test_function_returns_correct_result(self):
        actual = insert_into("helloo", "ce")
        self.assertEqual(actual, "helceloo")

        actual = insert_into("joy", "ce")
        self.assertEqual(actual, "joyce")


class ArrangWordTest(unittest.TestCase):
    def test_function_exists(self):
        arrange_word("sEmIClOn")

    def test_function_takes_only_string_type(self):
        with self.assertRaises(TypeError):
            arrange_word(2345)
            arrange_word([1,2,4])

    def test_function_returns_correct_result(self):
        actual = arrange_word("sEmIClOn")
        self.assertEqual(actual, "EICOsmln")

class CharcterCounterTest(unittest.TestCase):
    def test_function_exists(self):
        count_of("semicolon",'o')

    def test_function_takes_only_string_type(self):
        with self.assertRaises(TypeError):
            count_of("semicolon",2)
            count_of(12, "o")
            count_of(23, [])

    def test_function_returns_correct_result(self):
        actual = count_of("semicolon",'o')
        self.assertEqual(actual, ("o", 2))

class RemoveSpecialCharsTest(unittest.TestCase):
    def test_function_exists(self):
        remove_special_chars("he,ll,o")

    def test_function_takes_only_string_type(self):
        with self.assertRaises(TypeError):
            remove_special_chars(1)

    def test_function_returns_correct_result(self):
        actual = remove_special_chars("he,ll,o")
        self.assertEqual(actual, "hello")