"""
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""


def longest_distinct_subarray(arr: list[int]) -> int:
    largest_set = set()
    ans = 0
    for num in arr:
        if num in largest_set:
            ans = max(ans, len(largest_set))
            largest_set = set()
        largest_set.add(num)

    return max(ans, len(largest_set))


if __name__ == "__main__":
    print(longest_distinct_subarray([5, 1, 3, 5, 2, 3, 4, 1]))
    print(longest_distinct_subarray([1, 2, 3, 1, 2, 3, 4]))
    print(longest_distinct_subarray([1, 2, 3, 1, 6]))
