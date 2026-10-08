"""Tests for list1."""

import unittest
import list1


class TestDivisible(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(list1.divisible([1, 2, 3, 4, 5, 6], 2), [2, 4, 6])

    def test_empty_list(self):
        self.assertEqual(list1.divisible([], 5), [])

    def test_divisor_zero(self):
        with self.assertRaises(ValueError):
            list1.divisible([1, 2], 0)

    def test_first_argument_isnot_list(self):
        with self.assertRaises(TypeError):
            list1.divisible("1", 1)

    def test_divisor_not_int(self):
        with self.assertRaises(TypeError):
            list1.divisible([1, 2], 2.0)

    def test_float_argument(self):
        with self.assertRaises(TypeError):
            list1.divisible([1, 2.5, 3, 4, 5, 6], 1)


class TestCommon(unittest.TestCase):

    def test_match(self):
        self.assertEqual(list1.common([1, 2, 3], [2, 3, 4]), [2, 3])

    def test_match_empty(self):
        self.assertEqual(list1.common([], []), [])

    def test_match_duplicate(self):
        self.assertEqual(list1.common([1, 2, 3, 2], [2, 3, 4]), [2, 3])

    def test_nothing_in_common(self):
        self.assertEqual(list1.common([1, 2], [3, 4]), [])

    def test_smaller_count_wins(self):
        self.assertEqual(list1.common([1, 1, 2, 3], [1, 1, 1, 3, 4]),
                         [1, 1, 3])

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            list1.common(5, [2])
        with self.assertRaises(TypeError):
            list1.common([2], None)


if __name__ == "__main__":
    unittest.main()