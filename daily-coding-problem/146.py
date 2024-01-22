"""
Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

  0
 / \
1   0
    / \
   1   0
      / \
     0   0
should be pruned to:

  0
 / \
1   0
   /
  1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
"""

# create a function that detects an all-zero subtree
# checks children if value is zero, if yes recure, if no children, return true
# all else return false

# if true, remove all children of node
# if false, run method on children


class Node:
    def __init__(self, value: int, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def is_subtree_zeroed(node: Node) -> bool:
    if node.value == 0 and node.left is None and node.right is None:
        return True
    
    if node.left == 0 and node.right == 0:
        return is_subtree_zeroed(node.left) or is_subtree_zeroed(node.right)
    elif node.left == 0 and node.right is None:
        return is_subtree_zeroed(node.left)
    elif node.right == 0 and node.left is None:
        return is_subtree_zeroed(node.right)
    
    return False
    

def prune(root: Node):
    if is_subtree_zeroed(root):
        root.left = None
        root.right = None
    else:
        if root.left is not None and root.right is not None:
            prune(root.left)
            prune(root.right)
        elif root.left is not None:
            prune(root.left)
        elif root.right is not None:
            prune(root.right)


if __name__ == "__main__":
    tree = Node(0, Node(1), Node(0, Node(1, Node(0), Node(0)), Node(0)))
    print(tree.right.left.right.value)
    print(tree.right.left.left.value)
    prune(tree)
    print(tree.right.left.right.value)
    print(tree.right.left.left.value)