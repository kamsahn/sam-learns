"""
You are given an array of non-negative integers that represents a
two-dimensional elevation map where each element is unit-width wall and the
integer is the height. Suppose it will rain and all spots between two walls get
filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1)
space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the
middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2
in the second, and 3 in the fourth index (we cannot hold 5 since it would run
off to the left), so we can trap 8 units of water.
"""

# find the local/absolute max?
# take note of first wall height -> +/- from there

def water_walls(walls):
    h_max = 0
    total_water = 0
    tentative_water = 0
    for i in range(len(walls)):
        if walls[i] >= h_max:
            h_max = walls[i]
            total_water += tentative_water
            tentative_water = 0
        elif walls[i] < h_max:
            tentative_water += h_max - walls[i]

    return total_water

def water_walls_i(walls):
    total_water, left, right, tentative_water, i = 0, 0, 0, 0, 0
    while i < len(walls):
        if left == 0 and walls[i] > 0:
            left = walls[i]
            while right == 0:
                i += 1
                if walls[i] < left:
                    tentative_water +=


print("Input: [2, 1, 2], Expected: 1, Result:", water_walls([2, 1, 2]))  #  valley
print("Input: [3, 0, 1, 3, 0, 5], Expected: 8, Result:", water_walls([3, 0, 1, 3, 0, 5]))  # complex
print("Input: [3, 0, 1, 3, 0, 0], Expected: 5, Result:", water_walls([3, 0, 1, 3, 0, 0]))  # valley and cliff
print("Input: [0, 0, 1, 3, 0, 0], Expected: 0, Result:", water_walls([0, 0, 1, 3, 0, 0]))  # peak
print("Input: [5, 0, 0, 0, 0, 0], Expected: 0, Result:", water_walls([5, 0, 0, 0, 0, 0]))  # left cliff
print("Input: [0, 0, 0, 0, 0, 0], Expected: 0, Result:", water_walls([0, 0, 0, 0, 0, 0]))  # plateau
print("Input: [0, 0, 0, 0, 0, 5], Expected: 0, Result:", water_walls([0, 0, 0, 0, 0, 5]))  # right cliff
print("Input: [2, 1, 4, 1, 0, 2, 3], Expected: 7, Result:", water_walls([2, 1, 4, 1, 0, 2, 3]))  # complex

