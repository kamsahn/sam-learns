"""
There is an N by M matrix of zeroes.
Given N and M,
write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner.
You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""

# recursive checks if current position is less than M x N in either direction
# keep counter going


def ways_down_right(M: int, N: int) -> int:
    def helper(m: int = 1, n: int = 1, counter: int = 0) -> int:
        if m < M and n < N:
            return helper(m+1, n, counter+1) + helper(m, n+1, counter+1) - (counter+1)
        elif m < M:
            counter += 1
            return helper(m+1, n, counter+1)
        elif n < N:
            counter += 1
            return helper(m, n+1, counter+1)
        else:
            return counter
    
    return helper()


if __name__ == "__main__":
    print(ways_down_right(2, 2))
    print(ways_down_right(5, 5))
            