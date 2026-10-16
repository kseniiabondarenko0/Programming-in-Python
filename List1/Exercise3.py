import unittest


def subsets(x):
    """Write function subsets(x, y) that, for a given set x, returns a list of all its subsets. For
    example, for x = {a, b, c, d}, the function should return {a, b, c, d}, {a, b, c},
    {a, b, d}, {a, c, d}, {b, c, d}, {a, b}, {a, c}, {a, d}, {b, c}, {b, d}, {c, d},
    {a}, {b}, {c}, {d}, {}, in any order.

    :returns list: A list of all subsets of x"""

    if type(x) != set:
        raise TypeError("First argument must be a set.")

    result = [set()]

    for element in x:
        new_sets = []
        for subset in result:
            subsetA = set(subset)
            subsetA.add(element)
            new_sets.append(subsetA)
        result = result + new_sets

    return result

class TestSubsets(unittest.TestCase):

    def test_count(self):
        self.assertEqual(len(subsets({"a", "b", "c", "d"})), 16)

    def test_has_empty(self):
        self.assertIn(set(), subsets({"a", "b"}))

    def test_has_full(self):
        self.assertIn({"a", "b"}, subsets({"a", "b"}))

    def test_one_element(self):
        self.assertEqual(len(subsets({"a"})), 2)

    def test_empty_input(self):
        self.assertEqual(subsets(set()), [set()])

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            subsets([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
