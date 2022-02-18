"""
Given the root to a binary search tree, find the second largest node in the tree.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def second_largest_node(root):
    def check_max(node, l1, l2):
        if node.left:
            l1, l2 = check_max(node.left, l1, l2)
        if node.right:
            l1, l2 = check_max(node.right, l1, l2)
        if node.val > l1.val:
            l2 = l1
            l1 = node
        elif node.val > l2.val:
            l2 = node
        return l1, l2

    l1 = TreeNode(float('-inf'), None, None)
    l2 = None
    l1, l2 = check_max(root, l1, l2)
    return l2

n8 = TreeNode(1, None, None)
n7 = TreeNode(3, None, None)
n6 = TreeNode(2, None, None)
n5 = TreeNode(6, None, n8)
n4 = TreeNode(4, None, None)
n3 = TreeNode(1, n7, None)
n2 = TreeNode(5, n5, n6)
n1 = TreeNode(2, n3, n4)
n0 = TreeNode(1, n1, n2)

print('Node object:', second_largest_node(n0))
print('Node has a value of 5:', second_largest_node(n0).val == 5)
print('Node has a left leaf with a value of 6:', second_largest_node(n0).left.val == 6)
print('Node has a right leaf with a value of 2:', second_largest_node(n0).right.val == 2)


