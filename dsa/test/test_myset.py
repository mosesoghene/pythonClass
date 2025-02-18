import unittest

from src.myset import MySet


class MySetTest(unittest.TestCase):
    def test_myset_object_can_be_created(self):
        myset = MySet(3)

    def test_myset_object_can_be_initialized(self):
        myset = MySet(3)
        self.assertEqual(3, len(myset))

    def test_add_xyza_raise_index_error(self):

        myset = MySet(3)
        myset.add(1)
        myset.add(2)
        myset.add(3)

        self.assertRaises(IndexError, myset.add, 4)

    def test_add_xy_get_z_raise_index_error(self):
        myset = MySet(3)
        myset.add(1)
        myset.add(2)
        self.assertRaises(IndexError,myset.get,2)

    def test_add_xx_size_remains_one(self):
        myset = MySet(3)
        myset.add(1)
        self.assertEqual(1, myset.size())

        myset.add(1)
        self.assertEqual(1, myset.size())


    def test_add_xy_get_x_return_x(self):
        myset = MySet(3)
        myset.add(1)
        myset.add(2)
        self.assertEqual(myset.get(0), 1)

    def test_add_xy_contains_y_return_true(self):
        myset = MySet(3)
        myset.add(1)
        myset.add(2)
        self.assertTrue(myset.contains(2))

    def test_add_xy_contains_z_return_false(self):
        myset = MySet(3)
        myset.add(1)
        myset.add(2)
        self.assertFalse(myset.contains(3))

    def test_add_xy_clear_return_size_3(self):
        myset = MySet(3)
        myset.add(1)
        myset.add(2)
        myset.clear()
        self.assertEqual(3, len(myset))

    def test_add_xzy_return_xyz(self):
        myset = MySet(3)
        myset.add(1)
        myset.add(3)
        myset.add(2)
        myset.sort()
        self.assertEqual([1,2,3], myset.values())

    def test_add_xy_get_index_x_return_0(self):
        myset = MySet(3)
        myset.add(1)
        myset.add(2)
        self.assertEqual(0, myset.index(1))

    def test_add_xy_remove_x_get_index_x_return_y(self):
        myset = MySet(3)
        myset.add(1)
        myset.add(2)
        myset.remove(1)
        self.assertEqual(0, myset.index(2))


if __name__ == '__main__':
    unittest.main()
