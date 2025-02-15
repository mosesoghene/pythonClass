import unittest

from src.array import Array


class MyTestCase(unittest.TestCase):
    def test_array_object_can_be_created(self):
        array = Array(3)

    def test_array_object_can_be_initialized(self):
        array = Array(3)
        self.assertEqual(3, len(array))

    def test_add_xyza_raise_index_error(self):

        array = Array(3)
        array.add(1)
        array.add(2)
        array.add(3)

        self.assertRaises(IndexError, array.add, 4)

    def test_add_xy_get_z_raise_index_error(self):
        array = Array(3)
        array.add(1)
        array.add(2)
        self.assertRaises(IndexError,array.get,2)

    def test_add_xy_get_x_return_x(self):
        array = Array(3)
        array.add(1)
        array.add(2)
        self.assertEqual(array.get(0), 1)

    def test_add_xy_contains_y_return_true(self):
        array = Array(3)
        array.add(1)
        array.add(2)
        self.assertTrue(array.contains(2))

    def test_add_xy_contains_z_return_false(self):
        array = Array(3)
        array.add(1)
        array.add(2)
        self.assertFalse(array.contains(3))

    def test_add_xy_clear_return_size_3(self):
        array = Array(3)
        array.add(1)
        array.add(2)
        array.clear()
        self.assertEqual(3, len(array))

    def test_add_xzy_return_xyz(self):
        array = Array(3)
        array.add(1)
        array.add(3)
        array.add(2)
        array.sort()
        self.assertEqual([1,2,3], array.values())

    def test_add_xy_get_index_x_return_0(self):
        array = Array(3)
        array.add(1)
        array.add(2)
        self.assertEqual(0, array.index(1))

    def test_add_xy_remove_x_get_index_x_return_y(self):
        array = Array(3)
        array.add(1)
        array.add(2)
        array.remove(1)
        self.assertEqual(0, array.index(2))


if __name__ == '__main__':
    unittest.main()
