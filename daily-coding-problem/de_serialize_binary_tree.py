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

class Node():
    def __init__(self, val, left=None, right=None):
        """
        :param val: int, value of node
        :param left: Node, left node
        :param right: Node, right node
        """
        self.val = val
        self.left = left
        self.right = right

# def serialize_helper(node, counter):
#     counter += 1
#     s = f'val{counter}:{node.val},'
#     if node.left is not None:
#         s += f'left{counter}:{serialize_helper(node.left, counter)},'
#     if node.right is not None:
#         s += f'right{counter}:{serialize_helper(node.right, counter)},'
#     return s
#
# def deserialize_helper(s, counter):
#     val, left, right = '', None, None
#     ser_list = [e for e in s.split(',') if e != '']
#
#     counter += 1
#     for ser in ser_list:
#         pair_list = ser.split(':')
#
#         if str(counter) in pair_list[0]:
#             key = pair_list[0][:-1]
#
#             if key == 'val':
#                 print(val)
#             elif key == 'left':
#                 print(ser_list, counter)
#                 left = deserialize_helper(s, counter)
#             elif key == 'right':
#                 right = deserialize_helper(s, counter)
#
#     return Node(val, left, right)
#
# def serialize(node):
#     return serialize_helper(node, -1)
#
# def deserialize(s):
#     return deserialize_helper(s, -1)


"""
After reading about a serialization strategy
store node values in an array
first index is the root node value
next is its left node value and any of its left node values and any of its left node values...
until a node has no left node value, then enter its right node value
then do the same for that node until values are null and move up another level

for example:

Input:
         20
       /
      8
     / \
    4  12
      /  \
     10  14
Output: 20 8 4 -1 -1 12 10 -1 -1 14 -1 -1 -1
"""

# using Node class definition from above

def serialize(node):
    """
    :param node: Node object
    """
    def serialize_helper(node, serial):
        # node value
        serial += f'{node.val},'

        # left nodes
        if node.left is not None:
            serial = serialize_helper(node.left, serial)
        else:
            serial += f'-1,'
        # right nodes
        if node.right is not None:
            serial = serialize_helper(node.right, serial)
        else:
            serial += f'-1,'

        return serial

    return serialize_helper(node, '')[:-1]  # remove trailing comma

def deserialize(serial):
    """
    :param serial: str, serialized node object
        e.g. 'root,left,left.left,-1,-1,-1,right,-1,-1'
    """
    def deserialize_helper(sl, i):
        if i >= len(sl):
            return None
        # node = Node(sl[0], Node(sl[1], Node(sl[2], None, None), None), Node(sl[6], None, None))
        if sl[i] != '-1':
            node = Node(sl[i], deserialize_helper(sl, i+1), deserialize_helper(sl, i+1))
        else:
            node = None
        return node

    i = 0
    sl = serial.split(',')  # serialized list
    node = deserialize_helper(sl, i)

    return node




node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
print('')
print(deserialize(serialize(node)).right)
print(deserialize(serialize(node)).right.val)
print(deserialize(serialize(node)).right.right)
print(deserialize(serialize(node)).right.right.val)
print(deserialize(serialize(node)).right.right.right)
print('')
print(deserialize(serialize(node)).left)
print(deserialize(serialize(node)).left.left)
print(deserialize(serialize(node)).left.left.val)
print(deserialize(serialize(node)).left.left.left)



assert deserialize(serialize(node)).left.left.val == 'left.left'
assert deserialize(serialize(node)).right
assert deserialize(serialize(node)).right.right == None





