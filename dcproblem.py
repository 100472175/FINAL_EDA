import sys


def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    # Returns the first and last index of a given value in a list
    # If the value is not in the list, return (-1, -1)
    # If the value is in the list, return the first and last index of the value
    # If the value is in the list, but only once, return the first and last index of the value

    if a is None or len(a) == 0 or x is None:
        return -1, -1  # There is no need to put a parenthesis here, as it is the default return value
    result1, result2 = _find_first_last(a, x, 0, len(a) - 1)

    if result1 == sys.maxsize:
        result1 = -1
    if result2 == sys.maxsize:
        result2 = -1

    return result1, result2



def _find_first_last(array, x, start, end):
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
        return sys.maxsize, sys.maxsize


    """if first_last1[0] < first_last2[0]:
        a = first_last1[0]  # a is the first index of x in the list
    else:
        a = first_last2[0]  # a is the first index of x in the list

    if first_last1[1] > first_last2[1]:
        b = first_last1[1]
    else:
        b = first_last2[1]

    return a, b"""


    """if first_last1[0] != -1:
        return first_last1[0], first_last1[1]
    elif first_last2[0] != -1:
        return first_last2[0], first_last2[1]
    else:
        return -1, -1"""


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
