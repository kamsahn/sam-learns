"""
A fixed point in an array is an element whose value is equal to its index. 
Given a sorted array of distinct elements, return a fixed point, if one exists. 
Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. 
Given [1, 5, 7, 8], you should return False.
"""

def find_fixed_point(arr: list[int]) -> int:
    for i in range(len(arr)):
        if arr[i] == i:
            return i
        if arr[i] > i:
            return False
    return False


if __name__ == "__main__":
    print(find_fixed_point([-6, 0, 2, 40]))    
    print(find_fixed_point([1, 5, 7, 8]))
    print(find_fixed_point([1]))
    print(find_fixed_point([-2, -1, 0, 1, 4]))