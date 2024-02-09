"""
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""


def greatest_common_denominator(nums: list[int]) -> int:
    lowest_num = min(nums)
    for i in range(lowest_num, 1, -1):
        common_denominators = [num for num in nums if num % i == 0]
        if len(nums) == len(common_denominators):
            return i
                
    return 1


if __name__ == "__main__":
    print(greatest_common_denominator([42, 56, 14]))
    print(greatest_common_denominator([42, 56, 14, 6]))
    print(greatest_common_denominator([5, 4, 3]))
    print(greatest_common_denominator([45, 30]))
