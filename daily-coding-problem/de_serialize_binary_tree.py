"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.
For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

"""
WIP
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize_helper(node, counter):
    counter += 1
    s = f'val{counter}:{node.val},'
    if node.left is not None:
        s += f'left{counter}:{serialize_helper(node.left, counter)},'
    if node.right is not None:
        s += f'right{counter}:{serialize_helper(node.right, counter)},'
    return s

def deserialize_helper(s, counter):
    val, left, right = '', None, None
    ser_list = [e for e in s.split(',') if e != '']

    counter += 1
    for ser in ser_list:
        pair_list = ser.split(':')

        if str(counter) in pair_list[0]:
            key = pair_list[0][:-1]

            if key == 'val':
                print(val)
            elif key == 'left':
                print(ser_list, counter)
                left = deserialize_helper(s, counter)
            elif key == 'right':
                right = deserialize_helper(s, counter)

    return Node(val, left, right)

def serialize(node):
    return serialize_helper(node, -1)

def deserialize(s):
    return deserialize_helper(s, -1)


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
deserialize(serialize(node))

