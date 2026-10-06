"""List 1: Python basics for Java programmers (Programming in Python 2026/2027).

Exercises 1-2.
"""

from collections import Counter


def divisible(numbers, divisor):
    """Return the numbers from a list that are divisible by a given divisor.

    Args:
        numbers (list[int]): List of integers to filter.
        divisor (int): The integer to test divisibility by.

    Returns:
        list[int]: New list with those elements of ``numbers`` that are
        divisible by ``divisor``, in their original order (duplicates kept).

    Raises:
        TypeError: If ``numbers`` is not a list, or if any element of it or
            ``divisor`` is not an integer.
        ValueError: If ``divisor`` is zero.

    Preconditions:
        ``numbers`` is a list of integers; ``divisor`` is a non-zero integer.

    Postconditions:
        The input list is not modified. Every element of the result is in
        ``numbers`` and satisfies ``element % divisor == 0``.
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if not _is_int(divisor):
        raise TypeError("divisor must be an integer")
    if divisor == 0:
        raise ValueError("divisor must not be zero")
    if not all(_is_int(n) for n in numbers):
        raise TypeError("all elements of numbers must be integers")

    return [n for n in numbers if n % divisor == 0]


def common(x, y):
    """Return the intersection of two multisets.

    A multiset is represented as a list (or tuple) of hashable elements in
    which an element may occur many times. An element occurring ``a`` times in
    ``x`` and ``b`` times in ``y`` occurs ``min(a, b)`` times in the result.

    Args:
        x (list | tuple): First multiset.
        y (list | tuple): Second multiset.

    Returns:
        list: Multiset intersection of ``x`` and ``y``. Elements are ordered
        by their first occurrence in ``x``.

    Raises:
        TypeError: If ``x`` or ``y`` is not a list or tuple, or contains
            unhashable elements.

    Preconditions:
        ``x`` and ``y`` are lists or tuples of hashable elements.

    Postconditions:
        Inputs are not modified. The result is a sub-multiset of both ``x``
        and ``y`` and is the largest such multiset.

    Example:
        >>> common([1, 1, 2, 3], [1, 1, 1, 3, 4])
        [1, 1, 3]
    """
    for name, ms in (("x", x), ("y", y)):
        if not isinstance(ms, (list, tuple)):
            raise TypeError(f"{name} must be a list or tuple")
    try:
        count_x = Counter(x)
        count_y = Counter(y)
    except TypeError as err:
        raise TypeError("multiset elements must be hashable") from err

    # Counter '&' takes the minimum multiplicity of each element.
    shared = count_x & count_y
    result = []
    for element in count_x:  # insertion order = first occurrence in x
        result.extend([element] * shared[element])
    return result


def _is_int(value):
    """Return True if ``value`` is an int and not a bool."""
    return isinstance(value, int) and not isinstance(value, bool)
