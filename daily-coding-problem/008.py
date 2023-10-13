"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """

class Node:
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def count_unival(node):
    count = 0

    def count_unival_helper(node, count):
        if node.left is None and node.right is None:
            count += 1
        else:
            if node.left is not None and node.right is not None:
                if node.val == node.left.val == node.right.val:
                    count += 1
                count += count_unival_helper(node.left, 0)
                count += count_unival_helper(node.right, 0)
            elif node.left is not None:
                if node.val == node.left.val:
                    count += 1
                count += count_unival_helper(node.left, 0)
            elif node.left is None:
                if node.val == node.right.val:
                    count += 1
                count += count_unival_helper(node.right, 0)

        return count

    return count_unival_helper(node, count)



tree1 = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
tree2 = Node(5, Node(1, Node(5), Node(5)), Node(5, None, Node(5)))
tree3 = Node(5, Node(4, Node(4), Node(4)), Node(5, None, Node(5)))
tree4 = Node('a', Node('a'), Node('a', Node('a'), Node('a', None, Node('A'))))
print(count_unival(tree1))
print(count_unival(tree2))
print(count_unival(tree3))
print(count_unival(tree4))