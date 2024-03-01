"""
You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers.
For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

1
2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value,
eventually ending with an entry on the bottom row.
For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
"""


def find_max_weight(tri: list[list[int]],
                    row: int = 0,
                    i: int = 0,
                    ans: int = None) -> int:
    
    if ans is None:
        ans = tri[row][i]  # initialize weight at top

    if row + 1 == len(tri):
        return ans  # return ans at bottom of triangle
    
    next_row = tri[row + 1]
    
    return max(
        find_max_weight(tri, row + 1, i, ans + next_row[i]),
        find_max_weight(tri, row + 1, i + 1, ans + next_row[i + 1])
    )


if __name__ == "__main__":
    print(find_max_weight([[1], [2, 3], [1, 5, 1]]))
    print(find_max_weight([[1], [2, 3], [5, 1, 1]]))
    print(find_max_weight([[1], [2, 3], [5, 1, 1], [1, 1, 3, 5]]))
