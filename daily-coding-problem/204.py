"""
Given a complete binary tree, count the number of nodes in faster than O(n) time.
Recall that a complete binary tree has every level filled except the last,
and the nodes in the last level are filled starting from the left.
"""

# keep track of level?


class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def num_nodes(tree: Node) -> int:
    """O(n) time complexity"""
    if tree.left and tree.right:
        return num_nodes(tree.left) + num_nodes(tree.right) + 1
    elif tree.left:
        return num_nodes(tree.left) + 1
    elif tree.right:
        return num_nodes(tree.right) + 1
    else:
        return 1

def num_nodes2(tree: Node) -> int:
    # check the right side until we find no branch
    # keep track of level and multiply it by amount of necessary branches
    def level_counter(node: Node, level: int = 1) -> tuple[int, bool]:
        if node.right:
            return level_counter(node.right, level + 1)
        else:
            # if present left branch -> last node is partially filled out and there is one more level
            # if missing left branch -> last node is filled out and there are no more levels
            return (level+1, False) if node.left else (level, True)
                
    level, full = level_counter(tree)
    return (2**level) - 1 if full else (2**level) - 2


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6)))
    """
        1
       /\
      2  5
     /\  /\
    3 4 6
    """
    print(num_nodes2(tree))
    
    branch1 = Node(1, Node(2), Node(3))
    branch2 = Node(4, Node(5), Node(6))
    branch3 = Node(7, Node(8), Node(9))
    branch4 = Node(10, Node(11), Node(12))
    tree = Node(15, Node(14, branch1, branch2), Node(13, branch3, branch4))
    print(num_nodes2(tree))
