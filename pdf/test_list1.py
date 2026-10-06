"""Tests for list1 (Exercises 1-2)."""

import unittest

import list1


class TestDivisible(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(list1.divisible([1, 2, 3, 4, 5, 6], 2), [2, 4, 6])

    def test_none_divisible(self):
        self.assertEqual(list1.divisible([1, 3, 5], 2), [])

    def test_all_divisible(self):
        self.assertEqual(list1.divisible([3, 6, 9], 3), [3, 6, 9])

    def test_empty_list(self):
        self.assertEqual(list1.divisible([], 5), [])

    def test_zero_and_negatives(self):
        self.assertEqual(list1.divisible([-6, -3, 0, 3, 7], 3), [-6, -3, 0, 3])
        self.assertEqual(list1.divisible([4, -4, 5], -2), [4, -4])

    def test_divisor_one(self):
        self.assertEqual(list1.divisible([1, 2, 3], 1), [1, 2, 3])

    def test_duplicates_and_order_kept(self):
        self.assertEqual(list1.divisible([4, 2, 4, 3], 2), [4, 2, 4])

    def test_input_not_modified(self):
        data = [1, 2, 3, 4]
        list1.divisible(data, 2)
        self.assertEqual(data, [1, 2, 3, 4])

    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            list1.divisible([1, 2], 0)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            list1.divisible("123", 1)
        with self.assertRaises(TypeError):
            list1.divisible([1, 2], 2.0)
        with self.assertRaises(TypeError):
            list1.divisible([1, 2.5], 1)
        with self.assertRaises(TypeError):
            list1.divisible([1, True], 1)
        with self.assertRaises(TypeError):
            list1.divisible([1, 2], None)


class TestCommon(unittest.TestCase):
    def assertMultisetEqual(self, a, b):
        self.assertCountEqual(a, b)

    def test_typical(self):
        self.assertMultisetEqual(list1.common([1, 1, 2, 3], [1, 1, 1, 3, 4]),
                                 [1, 1, 3])

    def test_min_multiplicity(self):
        self.assertMultisetEqual(list1.common(["a"] * 3, ["a"] * 2), ["a", "a"])
        self.assertMultisetEqual(list1.common(["a"] * 2, ["a"] * 3), ["a", "a"])

    def test_disjoint(self):
        self.assertEqual(list1.common([1, 2], [3, 4]), [])

    def test_empty(self):
        self.assertEqual(list1.common([], [1, 2]), [])
        self.assertEqual(list1.common([1, 2], []), [])
        self.assertEqual(list1.common([], []), [])

    def test_identical(self):
        self.assertMultisetEqual(list1.common([1, 2, 2], [2, 1, 2]), [1, 2, 2])

    def test_symmetric(self):
        x, y = [1, 1, 2, 5, 5], [5, 1, 1, 1, 9]
        self.assertMultisetEqual(list1.common(x, y), list1.common(y, x))

    def test_tuples_and_strings(self):
        self.assertMultisetEqual(list1.common(("a", "b", "b"), ["b", "b", "c"]),
                                 ["b", "b"])

    def test_inputs_not_modified(self):
        x, y = [1, 1, 2], [1, 2, 2]
        list1.common(x, y)
        self.assertEqual(x, [1, 1, 2])
        self.assertEqual(y, [1, 2, 2])

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            list1.common(5, [1])
        with self.assertRaises(TypeError):
            list1.common([1], None)
        with self.assertRaises(TypeError):
            list1.common([[1], [2]], [[1]])  # unhashable elements


if __name__ == "__main__":
    unittest.main()
