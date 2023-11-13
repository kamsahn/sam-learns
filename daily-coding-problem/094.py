"""
Given a binary tree of integers,
find the maximum path sum between two nodes.
The path must go through at least one node,
and does not need to go through the root.
"""

"""
starting at the root,
descend the tree,
sum each two nodes,
keep track of max
"""


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_pair(root: Node):
    def max_helper(node: Node, ans: int = 0):
        if node.left and node.right:
            ans = max(node.left.value + node.value, node.right.value + node.value, ans)
            return max(max_helper(node.left, ans), max_helper(node.right, ans))
        elif node.left:
            ans = max(node.left.value + node.value, ans)
            return max_helper(node.left, ans)
        elif node.right:
            ans = max(node.right.value + node.value, ans)
            return max_helper(node.right, ans)
        return ans
    return max_helper(root)


if __name__ == "__main__":
    """
         1
        / \
       3   2
      / \ / \
     2  1 5  3
            / \
           3   2
    """
    tree = Node(1, Node(3, Node(2), Node(1)), Node(2, Node(5), Node(3, Node(3), Node(2))))
    print(max_pair(tree))
    
    tree = Node(1, Node(3, Node(2), Node(1)), Node(2, Node(5), Node(3, Node(5), Node(2))))
    print(max_pair(tree))
    
    tree = Node(1, Node(3, Node(2), Node(1)), Node(2, Node(1), Node(3, Node(3), Node(2))))
    print(max_pair(tree))
    
