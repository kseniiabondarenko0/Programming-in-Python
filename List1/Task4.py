import random
import unittest

import matplotlib.pyplot as plt



def random_walk(n):
    """A very lost walker leaves (0, 0) and stumbles one step at a time until he is more than n units from home

    Args:
        n (int): Distance from the centre at which the walker gives up. Must be > 0

    Returns:
        list: Positions as (x, y) tuples after each step; the last one is farther than n from (0, 0)

    Raises:
        TypeError: If n is not an int.
        ValueError: If n <= 0.

    Precondition: n is a positive integer
    Postcondition: Every step moves exactly 1 unit (left, right, up or down)
    and only the last point lies outside the circle of radius n
    """

    if type(n) != int:
        raise TypeError("n must be an integer.")
    if n <= 0:
        raise ValueError("n must be greater than 0.")

    x = 0
    y = 0
    coordinates = []
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while(x**2 + y**2 <= n**2):
        dx, dy = random.choice(steps)
        x += dx
        y += dy
        coordinates.append((x, y))
    return coordinates



class TestRandomWalk(unittest.TestCase):

    def testWrongType(self):
        with self.assertRaises(TypeError):
            random_walk("5")

    def testEmpty(self):
        with self.assertRaises(ValueError):
            random_walk(0)

    def testReturnList(self):
        result = random_walk(10)
        self.assertIsInstance(result, list)



if __name__ == "__main__":
    unittest.main(exit=False)

    n = 100
    coordinates = random_walk(n)
    x, y = zip(*coordinates)
    plt.plot(x, y, marker='o', linestyle='-', markersize=2)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Walker\'s Trajectory')
    plt.grid(True)
    plt.show()


    #couldn't start properly, only from the Terminal by using
    # cd List1
    # python Task4.py
