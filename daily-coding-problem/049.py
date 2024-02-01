"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""


# not in o(n) time:
def get_max_sum(arr: list) -> int:
    max_sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            max_sum = max(max_sum, sum(arr[i:j+1]))
    return max_sum


if __name__ == "__main__":
    print(get_max_sum([34, -50, 42, 14, -5, 86]))
    print(get_max_sum([-5, -1, -8, -9]))
            