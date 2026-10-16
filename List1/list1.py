import unittest


#Exercise 1
def divisible(numbers, divisor):
    """Returns x list of numbers from the input list that are divisible by the given divisor

    Do:
    Check if the divisor is zero, if the first argument is x list, and if the second argument is an integer

    Returns:
        list: A list of integers from the input list that are divisible by the given divisor
    """


    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    if type(numbers) != list:
        raise TypeError("First argument must be a list.")
    if type(divisor) != int:
        raise TypeError("Second argument must be an integer.")

    result = []
    for n in numbers:
        if type(n) != int:
            raise TypeError("List contains non-integer values.")
        if n % divisor == 0:
            result.append(n)

    return result


#Exercise 2
def common(x, y):


    """Return the intersection of multisets x & y
     Do: Check if the first argument is an x list, and if the second argument is a list
     Returns:
    list: A list of integers that are in both x and y"""


    if type(x) != list or type(y) != list:
        raise TypeError("Invalid input types. Must be lists.")

    list_y_copy = list(y)
    answer = []

    for element in x:
        if element in list_y_copy:
            answer.append(element)
            list_y_copy.remove(element)  # remove only one, so it is not counted twice
    return answer

