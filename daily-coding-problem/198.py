"""
Given a set of distinct positive integers, 
find the largest subset such that every pair of elements in the subset (i, j) satisfies either 
i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. 
Given [1, 3, 6, 24], return [1, 3, 6, 24].
"""

# nope

def find_largest_subset(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            inner_arr = arr[i:j]
            
            for k in range(len(inner_arr)):
                for l in range(k+1, len(inner_arr)+1):
                    print(inner_arr[k:l])
                


if __name__ == "__main__":
    find_largest_subset([3, 5, 10, 20, 21])
            