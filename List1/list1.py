"""Returns a list of numbers from the input list that are divisible by the given divisor

Do:
Check if the divisor is zero, if the first argument is a list, and if the second argument is an integer

Returns:
    list: A list of integers from the input list that are divisible by the given divisor
"""


#Exercise 1
def divisible(numbers, divisor):


    if divisor == 0:
        raise ValueError( "Error: Divisor cannot be zero.")
    if type(numbers) != list:
        raise TypeError("Error: First argument must be a list.")
    if type(divisor) != int:
        raise TypeError("Error: Second argument must be an integer.")


    result = []
    for n in numbers:
        if type(n) != int:
            return "Error: List contains non-integer values."
        if n%divisor == 0:
            result.append(n)

    return result




#Exercise 2

def common(a, y):
    if type(a)!=list or type(y)!=list:
        return "Error: Invalid input types.Must be lists"

    list_b_copy = list(y)
    answer = []

    for element in a:
        if element in list_b_copy:
            answer.append(element)
            list_b_copy.remove(element)  # remove only one, so it is not counted twice
    return answer


