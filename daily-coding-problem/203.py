"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
"""

# use binary search to find the split point faster


def find_rotation(arr: list[int]) -> int:
    start = arr[0]
    mid_index = len(arr) // 2
    
    while True:
        if len(arr) <= 2:
            # return smallest value
            # catch incase arr was never rotated
            return min(arr) if min(arr) < start else start

        else:
            if arr[mid_index] > start:
                arr = arr[mid_index:]
            elif arr[mid_index] < start:
                arr = arr[:mid_index+1]

            mid_index = len(arr) // 2

    
if __name__ == "__main__":
    print(find_rotation([5, 7, 8, 10, 3, 4]))
    print(find_rotation([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5]))
    print(find_rotation([4, 1, 2, 3]))
    print(find_rotation([1, 2, 3, 4]))
