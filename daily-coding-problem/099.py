"""
Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2],
the longest consecutive element sequence is [1, 2, 3, 4].
Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

# sort
# iterate and save longest sequence


def longest_sequence(nums: list) -> int:
    nums.sort()
    seq = []
    high_len = 0
    for num in nums:
        if len(seq) == 0:
            seq.append(num)
        else:
            if seq[-1] + 1 == num:
                seq.append(num)
            else:
                high_len = len(seq) if len(seq) > high_len else high_len
                seq = [num]
    return len(seq) if len(seq) > high_len else high_len


if __name__ == "__main__":
    print(longest_sequence([8, 100, 10, 11, 6, 4, 200, 1, 3, 7, 2, 9]))
    print(longest_sequence([1, 1, 1, 1, 1]))
    print(longest_sequence([3, 2, 1, 0]))
    print(longest_sequence([-3, -2, 2, 0, -1, 3]))
    print(longest_sequence([[0]]))
