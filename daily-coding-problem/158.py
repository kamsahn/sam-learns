"""
You are given an N by M matrix of 0s and 1s.
Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down.
0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
[0, 0, 1],
[1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.
"""

# use recursion
# store paths to check and split easily

# given that we always start with zero
# check down and right -> if any are not 1's, recure with that node added to the path
# path is only valid if last point is reached (matrix[N-1][M-1])

def ways_to_bottom(matrix) -> int:
    ways = 0
    N = len(matrix)
    M = len(matrix[0])
    end_point = N-1, M-1
    
    def ways_helper(start: tuple[int, int]):
        # made it to the end
        if start == end_point:
            return 1
        
        down = start[0] + 1, start[1]
        right = start[0], start[1] + 1

        # both options are valid
        if down[0] != N and right[1] != M:
            if matrix[down[0]][down[1]] == 0 and matrix[right[0]][right[1]] == 0:
                return ways_helper(down) + ways_helper(right)
                
        # just down is valid
        if down[0] != N:
            if matrix[down[0]][down[1]] == 0:
                return ways_helper(down)
            
        # just right is valid
        if right[1] != M:
            if matrix[right[0]][right[1]] == 0:
                return ways_helper(right)
        
        # nothing is valid
        return 0
    
    s = 0, 0
    ways += ways_helper(s)
    return ways


if __name__ == "__main__":
    matrix = [[0, 0, 1],
              [0, 0, 1],
              [1, 0, 0]]
    print(ways_to_bottom(matrix))
    
    matrix = [[0, 0, 0, 0],
              [0, 0, 1, 0],
              [1, 0, 0, 0]]
    print(ways_to_bottom(matrix))
    
    matrix = [[0, 0, 0, 0],
              [0, 0, 0, 1],
              [1, 0, 0, 0]]
    print(ways_to_bottom(matrix))
            