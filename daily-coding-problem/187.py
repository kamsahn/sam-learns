"""
You are given given a list of rectangles represented by min and max x- and y-coordinates.
Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
"top_left": (1, 4),
"dimensions": (3, 3) # width, height
},
{
"top_left": (-1, 3),
"dimensions": (2, 1)
},
{
"top_left": (0, 5),
"dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.
"""


def is_overlapping(top_left1: tuple[int, int],
                   dimensions1: tuple[int, int],
                   top_left2: tuple[int, int],
                   dimensions2: tuple[int, int],) -> bool:
    
    one_overlaps_two_x = top_left1[0] < top_left2[0] < (top_left1[0] + dimensions1[0])
    one_overlaps_two_y = top_left1[1] > top_left2[1] > (top_left1[1] - dimensions1[1])
    two_overlaps_one_x = top_left2[0] < top_left1[0] < (top_left2[0] + dimensions2[0])
    two_overlaps_one_y = top_left2[1] > top_left1[1] > (top_left2[1] - dimensions2[1])
    
    return True if ((one_overlaps_two_x and one_overlaps_two_y) or (two_overlaps_one_x and two_overlaps_one_y)) else False


def any_overlap(rectangles: list[dict]) -> bool:
    for i in range(len(rectangles)):
        for j in range(i+1, len(rectangles)):
            r1 = rectangles[i]
            r2 = rectangles[j]
            if is_overlapping(r1["top_left"], r1["dimensions"], r2["top_left"], r2["dimensions"]):
                return True
    return False


if __name__ == "__main__":
    rs = [
        {
            "top_left": (1, 4),
            "dimensions": (3, 3)
        },
        {
            "top_left": (-1, 3),
            "dimensions": (2, 1)
        },
        {
            "top_left": (0, 5),
            "dimensions": (4, 3)
        }
    ]
    print(any_overlap(rs))
    rs = [
        {
            "top_left": (1, 4),
            "dimensions": (3, 3)
        },
        {
            "top_left": (-1, 3),
            "dimensions": (2, 1)
        },
    ]
    print(any_overlap(rs))
