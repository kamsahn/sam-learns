"""
A wall consists of several rows of bricks of various integer lengths and uniform height.
Your goal is to find a vertical line going from the top to the bottom of the wall that cuts through the fewest number
of bricks. If the line goes through the edge between two bricks, this does not count as a cut.

For example, suppose the input is as follows, where values in each row represent the lengths of bricks in that row:

[[3, 5, 1, 1],
    [2, 3, 3, 2],
    [5, 5],
    [4, 4, 2],
    [1, 3, 3, 3],
    [1, 1, 6, 1, 1]]
The best we can we do here is to draw a line after the eighth brick, which will only require cutting through the bricks
in the third and fifth row.

Given an input consisting of brick lengths for each row such as the one above, return the fewest number of bricks that
must be cut to create a vertical line.
"""

# find which space can be cut without cutting a brick on each row
# the value with the most frequency is the answer


def least_bricks_cut(wall: list[list[int]]) -> int:
    safe = dict()
    for row in wall:
        agg = 0
        for i in range(len(row) - 1):  # don't add the "end" cut
            agg += row[i]
            if agg not in safe:
                safe[agg] = 0
            safe[agg] += 1
    
    return max(safe, key=safe.get)


if __name__ == "__main__":
    w = [
        [3, 5, 1, 1],
        [2, 3, 3, 2],
        [5, 5],
        [4, 4, 2],
        [1, 3, 3, 3],
        [1, 1, 6, 1, 1]
    ]
    print(least_bricks_cut(w))
    w = [
        [1, 1, 3, 5],
        [2, 3, 3, 2],
        [5, 5],
        [2, 4, 4],
        [3, 3, 3, 1],
        [1, 1, 6, 1, 1]
    ]  # reversed lay
    print(least_bricks_cut(w))
    w = [
        [2, 1],
        [1, 2],
        [2, 1],
        [2, 1],
        [2, 1],
        [3]
    ]
    print(least_bricks_cut(w))
    w = [
        [1, 1, 1, 1, 1],
        [5],
        [5],
        [4, 1],
    ]
    print(least_bricks_cut(w))
