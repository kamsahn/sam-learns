"""
Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
"top_left": (1, 4),
"dimensions": (3, 3) # width, height
}
and

{
"top_left": (0, 5),
"dimensions": (4, 3) # width, height
}
return 6.
"""

# top_left: (1, 4) + dimensions: (3, 3) -> bottom_right: (4, 1)
# top_left: (0, 5) + dimensions: (4, 3) -> bottom_right: (4, 2)

# take the lowest and most right point from the two top lefts
# take the highest and most left point from the two bottom rights
# get the area of that rectangle

def get_overlapping_area(r1: dict, r2: dict) -> int:
    # calc bottom right 
    r1_bottom_right = (r1["top_left"][0] + r1["dimensions"][0], r1["top_left"][1] - r1["dimensions"][1])
    r2_bottom_right = (r2["top_left"][0] + r2["dimensions"][0], r2["top_left"][1] - r2["dimensions"][1])
    
    if (r2_bottom_right[0] < r1["top_left"][0] and r2_bottom_right[1] > r1["top_left"][1]) or \
       (r1_bottom_right[0] < r2["top_left"][0] and r1_bottom_right[1] > r2["top_left"][1]):
        return 0
    
    ol_top_left = (max(r1["top_left"][0], r2["top_left"][0]), min(r1["top_left"][1], r2["top_left"][1]))
    ol_bottom_right = (min(r1_bottom_right[0], r2_bottom_right[0]), max(r1_bottom_right[1], r2_bottom_right[1]))
    
    # take area of overlapping rectangle
    ol_width = ol_bottom_right[0] - ol_top_left[0]
    ol_height = ol_top_left[1] - ol_bottom_right[1]
    
    return ol_width * ol_height


if __name__ == "__main__":
    r1 = {
        "top_left": (1, 4),
        "dimensions": (3, 3)
    }
    r2 = {
        "top_left": (0, 5),
        "dimensions": (4, 3)
    }
    print(get_overlapping_area(r1, r2))

    r1 = {
        "top_left": (3, 5),
        "dimensions": (1, 3)
    }
    r2 = {
        "top_left": (0, 7),
        "dimensions": (2, 1)
    }
    print(get_overlapping_area(r1, r2))
    
    r1 = {
        "top_left": (5, 5),
        "dimensions": (1, 1)
    }
    r2 = {
        "top_left": (1, 1),
        "dimensions": (1, 1)
    }
    print(get_overlapping_area(r1, r2))
