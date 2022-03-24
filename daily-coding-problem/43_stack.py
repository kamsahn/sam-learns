"""
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack

pop(), which pops off and returns the topmost element of the stack. If there
are no elements in the stack, then it should throw an error or return null.

max(), which returns the maximum value in the stack currently. If there are no
elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
"""

class Stack:
    """
    A stack data structure holds elements in a FILO order.
    i.e. the first element pushed to the stack will be the "bottom" of the
        stack while the latest element pushed will be the "top" of the stack.
    All methods (push, pop and max) will operate in constant time.
    """
    def __init__(self):
        self.elements = []
        self.max_elem = None

    def push(self, val):
        self.elements.append(val)
        if self.max_elem is not None:
            self.max_elem = max(self.max_elem, val)
        else:
            self.max_elem = val

    def pop(self):
        if len(self.elements):
            return self.elements.pop()
        else:
            return None

    def max(self):
        return self.max_elem


stack = Stack()
stack.push(2)
stack.push(4)
stack.push(6)
stack.push(3)
stack.push(4)
print("Popped element is 4:", stack.pop() == 4)
print("Max is 6", stack.max() == 6)
print("Popped element is 3:", stack.pop() == 3)

empty_stack = Stack()
print("Popping from empty stack returns None", empty_stack.pop() is None)
print("Taking the max of an empty stack returns None", empty_stack.max() is None)




