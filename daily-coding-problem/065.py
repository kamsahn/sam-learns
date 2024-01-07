"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
[6,  7,  8,  9,  10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""

# ugh

def sprial_print(matrix: list[list[int]]):
    row, column = 0, 0
    while row < len(matrix[0]):
        print(matrix[column][row])
        row += 1
    
    row -= 1
    column += 1
    while column < (len(matrix)):
        print(matrix[column][row])
        column += 1
    
    column -= 1
    row -= 1
    while row >= 0:
        print(matrix[column][row])
        row -= 1
    
    row += 1
    column -= 1
    while column >= 0:
        print(matrix[column][row])
        column -= 1
    
    
if __name__ == "__main__":
    matrix = [[1,  2,  3,  4,  5],
              [6,  7,  8,  9,  10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]]
    sprial_print(matrix)
            