"""
Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""


class MatrixIterator:
    def __init__(self, matrix: list[list]):
        self.matrix = matrix
        self.position = (0, 0)  # outer array index, inner array index
        self.outer_length = len(matrix)
    
    def has_next(self):
        # check next inner first
        inner_length = len(self.matrix[self.position[0]])
        if inner_length > self.position[1] + 1:
            if self.matrix[self.position[0]][self.position[1] + 1]:
                self.position = self.position[0], self.position[1] + 1
                return True
        
        self.position = self.position[0] + 1, 0
        # check next outer second
        if self.outer_length > self.position[0]:
            if self.matrix[self.position[0]][0]:
                return True
        
        return False
    
    def next(self):
        if self.has_next():
            print(self.matrix[self.position[0]][self.position[1]])


if __name__ == "__main__":
    iterator = MatrixIterator([[1, 2], [3], [], [4, 5, 6]])
    iterator.next()
    iterator.next()
    iterator.next()
    iterator.next()
    iterator.next()
    iterator.next()
    iterator.next()
