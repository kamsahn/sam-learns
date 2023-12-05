"""
You are given an N by M 2D matrix of lowercase letters.
Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically.
That is, the letter at each column is lexicographically later as you go down each row.
It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi
This is not ordered because of the a in the center.
We can remove the second column to make it ordered:

ca
df
gi
So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef
Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it.
"""

# if more than 1 row, break out into columns
# make each column a list and compare to a sorted version of the list
# if they don't match, add one to the counter
# return counter

def min_column_removed(matrix: list[str]) -> int:
    def helper(i: int = 0) -> int:
        # assemble column
        column = [row[i] for row in matrix]
        sorted_column = sorted(column)
        return 0 if column == sorted_column else 1
        
    if len(matrix) < 2:
        return 0
    
    counter = 0
    # for every element in row (assuming all rows are same length)
    for i in range(len(matrix[0])):
        counter += helper(i)
    
    return counter


if __name__ == "__main__":
    m = ['cba',
         'daf',
         'ghi']
    print(min_column_removed(m))
    m = ['abcdef']
    print(min_column_removed(m))
    m = ['zyx',
         'wvu',
         'tsr']
    print(min_column_removed(m))
    m = ['cbac',
         'daff',
         'ghie']
    print(min_column_removed(m))
    m = ['aaaaa',
         'aaaaa',
         'aaaaa']
    print(min_column_removed(m))
    m = ['bbbbb',
         'aaaaa',
         'aaaaa']
    print(min_column_removed(m))
