"""
Given an array of integers where every integer occurs three times except for
one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1.
Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""

def nondup(ints):
    nums = {}
    for i in ints:
        if not nums.get(i):
            nums[i] = 0
        nums[i] += 1
    return [i for i in nums if nums[i] == 1][0]

print(nondup([6, 1, 3, 3, 3, 6, 6]))