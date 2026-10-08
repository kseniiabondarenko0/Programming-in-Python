import unittest
import list1

class TestDivisible(unittest.TestCase):
    def test_match(self):
        self.assertEqual(list1.common([1, 2, 3], [2, 3, 4]), [2, 3])

    def test_match_empty(self):
        self.assertEqual(list1.common([], []), [])

    def test_match_duplicate(self):
        self.assertEqual(list1.common([1, 2, 3, 2], [2, 3, 4]), [2, 3])



