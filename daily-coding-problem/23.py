"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null.
You can move up, left, down, and right.
You cannot move through walls.
You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7,
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""

matrix = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False]
]

def shortest_path(matrix, start, end):
    """
    :param matrix: list(list), grid map where True is a wall and False is a path
    :param start: tuple, coordinate for start location
    :param end: tuple, coordinate for end location
    """
    current = start
    steps = 0
    if check_end():
        return steps

    def check_end():
        """compare current and end tuple"""
        if current == end:
            return True

    def check_wall(location):
        return True if matrix[location[0]][location[1]] else False

    def check_off_board():
        if current[0]+1 > len(matrix) or current[0] < 0 or current[1]+1 > len(matrix[0]) or current[1] < 0:
            return True
        return False

    def move(direction):
        """move the current location on given index"""
        # determine moving direction
        moving_i, stable_i = 0, 1 if direction == 0 else 1, 0

        current_coord = current[moving_i]
        end_coord = end[moving_i]
        if current_coord > end_coord:
            if not check_wall((current_coord-1, current[stable_i])):
                current = (current_coord-1, current[stable_i])
                steps += 1
                if check_end():
                    return steps
            else:
                current = (current[moving_i], current[stable_i]+1)
                if check_off_board():
                    current = (current[moving_i], current[stable_i]-2)
                return move(moving_i)

    return move(0)




