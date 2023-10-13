"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""

def highest_missing(res, store):
    res += 1
    return res if not store.get(res) else highest_missing(res, store)

def first_missing(l):
    # keep track of n with dict
    # keep track of lowest positive
    # time O(n) ??? worst case O(2n) which == O(n)...
    # space is not constant...?
    store = {}
    lowest = float('inf')
    for n in l:
        if not store.get(n):
            store[n] = True
        if n > 0:
            lowest = min(lowest, n)

    if lowest == float('inf'):
        return 1

    return highest_missing(lowest, store)


print(first_missing([3, 4, -1, 1]))
print(first_missing([1, 2, 0]))
print(first_missing([-3, -1, -5]))
print(first_missing([-5, -4, 2, 1, -6, 6]))
print(first_missing([7, 6, 5, 4]))
print(first_missing([4, 5, 6, 7]))