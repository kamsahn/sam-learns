"""
The problem definition was easy enough to follow and even marked as easy on leetcode. That did not stop me from getting
tripped up trying to find an efficient, complete way to solve this problem...
My mind didn't initially jump to hash tables -- a sign that doing these challenges is a good use of my time ;) -- so my
initial solution was much more brute-forcey. Admittedly the complement was portion was taken from leetcode which helped
out with the final implementation. I was only thinking addition which made it hard to get to the hash table solution.
Something to think about for future problems!
"""

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(nums, target):
    hash_table = {}
    for i, elem in enumerate(nums):
        complement = target - elem
        if isinstance(hash_table.get(complement), int):
            return [hash_table[complement], i]
        hash_table[elem] = i


if __name__ == "__main__":
    two_sum([2, 3, 22, 7, 11, 15], 9)
