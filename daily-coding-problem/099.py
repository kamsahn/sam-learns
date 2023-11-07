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
                high_len = max(len(seq), high_len)
                seq = [num]
    return max(len(seq), high_len)


# from online
def longest_sequence_2(nums: list) -> int:
    high_len = 0
    for num in nums:
        if (num - 1) not in nums:
            # num is the start of a sequence
            j = num
            while j in nums:
                j += 1
            high_len = max(high_len, j - num)
    return high_len



if __name__ == "__main__":
    print(longest_sequence([8, 100, 10, 11, 6, 4, 200, 1, 3, 7, 2, 9]))
    print(longest_sequence([1, 1, 1, 1, 1]))
    print(longest_sequence([3, 2, 1, 0]))
    print(longest_sequence([-3, -2, 2, 0, -1, 3]))
    print(longest_sequence([0]))

    print(longest_sequence_2([8, 100, 10, 11, 6, 4, 200, 1, 3, 7, 2, 9]))
    print(longest_sequence_2([1, 1, 1, 1, 1]))
    print(longest_sequence_2([3, 2, 1, 0]))
    print(longest_sequence_2([-3, -2, 2, 0, -1, 3]))
    print(longest_sequence_2([0]))
