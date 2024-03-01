"""
A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation.
For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array.
For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
"""

def apply_permutation(arr: list[any], permutation: list[int]) -> list[any]:
    ans = [None for _ in range(len(arr))]
    for i in range(len(arr)):
        ans[permutation[i]] = arr[i]

    return ans


if __name__ == "__main__":
    print(apply_permutation(["a", "b", "c"], [2, 1, 0]))
