"""
Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""
import math

# in the example, 1 does not appear more than half the time

# there will necessarily only be one element that does this
# at worst the first occurance will be at the center of the list
# try one element at a time, iterating from the front of the list

def find_majority_element(lst: list[int]) -> int:
    for elem in lst:
        elem_num = len([e for e in lst if e == elem])
        if elem_num > math.floor(len(lst) / 2.0):
            return elem


if __name__ == "__main__":
    print(find_majority_element([1, 2, 1, 1, 3, 4, 0, 1, 1]))
    print(find_majority_element([1, 2, 1, 2, 1, 3, 2, 4, 0, 2, 2, 2, 2]))
    print(find_majority_element([1, 1, 1, 3, 3, 3, 3]))


    