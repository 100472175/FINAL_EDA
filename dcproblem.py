# Eduardo Alarcón (100472175)
import sys


def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    # Returns the first and last index of a given value in a list
    # If the value is not in the list, return (-1, -1)
    # If the value is in the list, return the first and last index of the value
    # If the value is in the list, but only once, returns the same index

    if a is None or len(a) == 0 or x is None:
        return -1, -1  # There is no need to put a parenthesis here, as it is the default return value
    result1, result2 = _find_first_last(a, x, 0, len(a) - 1)

    if result1 == sys.maxsize:
        result1 = -1
    if result2 == sys.maxsize:
        result2 = -1

    return result1, result2


def _find_first_last(array, x, start, end):
    # Protection of code, if the end index is higher than the start index, returns the same as if there were
    # no elements found in the list
    if start > end:
        return -1, -1  # Parenthesis are not needed, as it is the default return value

    # Base case, when there is only one element inside the domain being analyzed
    if start == end:
        if array[start] == x:
            return start, start  # Same here
        else:
            return -1, -1  # Same here

    # Obtain the middle of the lists
    mid = (start + end) // 2

    # Recursion
    first_last1 = _find_first_last(array, x, start, mid)
    first_last2 = _find_first_last(array, x, mid + 1, end)

    # Merging the results
    if first_last1[0] != -1 and first_last2[0] != -1:
        return min(first_last1[0], first_last2[0]), max(first_last1[1], first_last2[1])
    elif first_last1[0] != -1:
        return first_last1[0], first_last1[1]
    elif first_last2[0] != -1:
        return first_last2[0], first_last2[1]
    else:
        return -1, -1


"""
    def _find_first_last2(array, x, start, end):
    # Function that uses sys.maxsize instead of -1 if the element do not exist in the list
    if start > end:
        return sys.maxsize, sys.maxsize  # We will later change it to -1, -1
    if start == end:
        if array[start] == x:
            return start, start  # There is no need to put a parenthesis here, as it is the default return value
        else:
            return sys.maxsize, sys.maxsize  # We will later change it to -1, -1

    mid = (start + end) // 2
    first_last1 = _find_first_last(array, x, start, mid)
    first_last2 = _find_first_last(array, x, mid + 1, end)

    if first_last1[0] != sys.maxsize and first_last2[0] != sys.maxsize:
        return min(first_last1[0], first_last2[0]), max(first_last1[1], first_last2[1])
    elif first_last1[0] != sys.maxsize:
        return first_last1[0], first_last1[1]
    elif first_last2[0] != sys.maxsize:
        return first_last2[0], first_last2[1]
    else:
        return sys.maxsize, sys.maxsize"""

# Worst iteration, failing with 1 occurrence, 2 occurrences and more than 2, F=(3, 4, 4_a, 5, 6, 6_a, 7, 8)
"""if first_last1[0] < first_last2[0]:
        a = first_last1[0]  # a is the first index of x in the list
    else:
        a = first_last2[0]  # a is the first index of x in the list

    if first_last1[1] > first_last2[1]:
        b = first_last1[1]
    else:
        b = first_last2[1]

    return a, b"""

# Failed : 7, passed 4 (Failed in 3, 4, 5, 6, 6_a, 7, 8)
"""if first_last1[0] != -1:
        return first_last1[0], first_last1[1]
    elif first_last2[0] != -1:
        return first_last2[0], first_last2[1]
    else:
        return -1, -1"""

# First iteration, with only some test running correctly Filed 7, passed 4(Failed in 3, 4, 5, 6, 6_a, 7, 8)
"""if first_last1[0] != -1:
        return first_last1
    if first_last2[0] != -1:
        return first_last2"""


if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4  # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)

    # These are the examples provided in the instruction PDF
    ltt1 = [-2, 3, -2, 3, 0, 1, 2, -1, -1, 5]
    ltt2 = []
    elements = [-2, 3, 0, -1, 4, 5, -2]

    print("For the list ltt1: ", ltt1)
    for value in elements:
        first, last = find_first_last(ltt1, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    print("For the list ltt2: ", ltt2)
    first, last = find_first_last(ltt2, -2)
    print("x: ", value, ", first index:", first, ", last index: ", last)

