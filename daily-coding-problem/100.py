"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

(x,y) to
(x+1, y),
(x - 1, y),
(x, y+1),
(x, y-1),
(x-1, y-1),
(x+1,y+1),
(x-1,y+1),
(x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1).
It takes one more step to move from (1, 1) to (1, 2).
"""

# if there is a difference between at least one current coordinate and next coordinates,
# increment/decrement current coordinate
# add a step


def move(start: tuple, end: tuple, i: int) -> tuple:
    # mutating a list, returning a tuple
    start_list = [start[0], start[1]]
    if end[i] - start[i] > 0:
        start_list[i] += 1
    else:
        start_list[i] -= 1
    return start_list[0], start_list[1]


def min_steps(points: list, current_p: tuple, next_index: int = 1, steps: int = 0) -> int:
    # define next point
    next_p = points[next_index]
    # check if at destination
    x_off_target = next_p[0] - current_p[0] != 0
    y_off_target = next_p[1] - current_p[1] != 0
    if x_off_target or y_off_target:
        # if not, take a step
        steps += 1
        if x_off_target:
            # x coord does not match, move x
            current_p = move(current_p, next_p, 0)
        if y_off_target:
            # y coord does not match, move y
            current_p = move(current_p, next_p, 1)
        # start again
        return min_steps(points, current_p, next_index, steps)
    else:
        # destination reached, define new destination if available
        next_index += 1
        if next_index == len(points):
            # no new destination, return answer
            return steps
        else:
            # define new starting, ending point
            return min_steps(points, points[next_index-1], next_index, steps)
        

if __name__ == "__main__":
    points = [(0, 0), (1, 1), (1, 2)]
    print("expected 2:", min_steps(points, points[0]))
    
    points = [(0, 0), (-1, -1), (1, 2)]
    print("expected 4:", min_steps(points, points[0]))

    points = [(3, 1), (-1, -1), (1, 2)]
    print("expected 7:", min_steps(points, points[0]))
    
    points = [(0, 0), (1, 1), (1, 2), (2, 2), (3, 3)]
    print("expected 4:", min_steps(points, points[0]))
