"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i
of the new array isthe product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""

def prod_at_index(l):
    """
    O(2n)
    ...
    O(n)
    """
    total_product = 1
    new_l = []
    for n in l:
        total_product *= n
    for i in range(len(l)):
        new_i = int(total_product / l[i])
        new_l.append(new_i)
    return new_l


def prod_at_index2(l):
    """
    O(n*2(n-1))
    ...
    O(n**2)
    """
    new_l = []
    for i in range(len(l)):
        new_l.append(1)
        temp_l = l[:i] + l[i+1:]  # O(n-1)
        for n in temp_l:  # O(n-1)
            new_l[i] *= n

    return new_l


print(prod_at_index2([1, 2, 3, 4, 5]))
print(prod_at_index2([3, 2, 1]))
