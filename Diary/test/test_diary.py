import unittest

from diary import Diary


class DiaryTest(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("og", "1234")

    def test_diary_is_unlocked_by_default(self):
        self.assertFalse(self.diary.is_locked)

    def test_diary_can_be_locked(self):
        self.assertFalse(self.diary.is_locked)
        self.diary.lock("1234")
        self.assertTrue(self.diary.is_locked)

    def test_that_diary_cannot_lock_with_incorrect_password(self):
        self.assertFalse(self.diary.is_locked)
        self.assertRaises(ValueError, self.diary.lock, "1233")

    def test_that_diary_cannot_unlock_with_incorrect_password(self):
        self.assertFalse(self.diary.is_locked)

        self.diary.lock("1234")
        self.assertTrue(self.diary.is_locked)

        self.assertRaises(ValueError, self.diary.unlock, "1233")

    def test_diary_can_be_unlocked(self):
        self.assertFalse(self.diary.is_locked)

        self.diary.lock("1234")
        self.assertTrue(self.diary.is_locked)

        self.diary.unlock("1234")
        self.assertFalse(self.diary.is_locked)

    def test_diary_entries_zero_by_default(self):
        self.assertFalse(self.diary.is_locked)
        self.assertEqual(0, self.diary.total_entries())

    def test_add_entry_increases_entries_length(self):
        self.assertFalse(self.diary.is_locked)
        self.assertEqual(0, self.diary.total_entries())

        self.diary.add_entry("Entry 1", "Entry 1 content")
        self.assertEqual(1, self.diary.total_entries())

    def test_that_add_entry_raises_error_when_diary_is_locked(self):
        self.assertFalse(self.diary.is_locked)

        self.diary.lock("1234")
        self.assertEqual(self.diary.total_entries(), 0)

        self.assertRaises(ValueError, self.diary.add_entry, "Entry 1", "Entry 1 content")

        self.assertEqual(self.diary.total_entries(), 0)

    def test_that_delete_entry_decreases_entries_length(self):
        self.assertFalse(self.diary.is_locked)

        self.diary.add_entry("Entry 1", "Entry 1 content")
        self.diary.add_entry("Entry 2", "Entry 2 content")
        self.assertEqual(2, self.diary.total_entries())

        self.diary.delete_entry(2, '1234')
        self.assertEqual(1, self.diary.total_entries())

        self.diary.add_entry("Entry 3", "Entry 3 content")
        self.assertEqual(2, self.diary.total_entries())

    def test_that_delete_entry_raises_error_when_diary_is_locked(self):
        self.assertFalse(self.diary.is_locked)

        self.diary.add_entry("Entry 1", "Entry 1 content")
        self.diary.add_entry("Entry 2", "Entry 2 content")
        self.assertEqual(2, self.diary.total_entries())

        self.diary.lock("1234")

        self.assertRaises(ValueError, self.diary.delete_entry, 2, '1234')
        self.assertEqual(2, self.diary.total_entries())