"""
Given an array of numbers,
find the length of the longest increasing subsequence in the array.
The subsequence does not necessarily have to be contiguous.

For example, given the array
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

# write a terribly ugly recursive method that looks for larger elements
# whenever we find a larger element, return max of current path and new path


def max_subsequence(arr: list[int], first: int, count: int = 1) -> int:
    """
    start count at 1 since the first element will be used in the sequence
    """
    for i in range(len(arr)):
        if arr[i] > first:
            return max(
                max_subsequence(arr[i:], arr[i], count+1),  # continue with the newly found high number
                max_subsequence(arr[i+1:], first, count)  # continue as if above number were skipped
            )
    return count


if __name__ == "__main__":
    a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]   # expected 6 => 0, 2, 6, 9, 11, 15
    print(max_subsequence(a, a[0]))
    a = [6, 5, 3, 8, 1, 3, 4, 9, 10, 2, 7, 12]  # expected 6 => 1, 3, 4, 9, 10, 12
    print(max_subsequence(a, a[0]))
            
