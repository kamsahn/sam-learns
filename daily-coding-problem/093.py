"""
Given a tree, find the largest tree/subtree that is a BST.
Given a tree, return the size of the largest tree/subtree that is a BST.
"""

"""
from the internet, BST defined as:
A straightforward approach to check if a binary tree is BST or not is to
check at every node,
the maximum value in the left subtree is less than the current node's value,
and the minimum value in the right subtree is greater than the current node's value.

starting from root,
check each subtree if it is a BST
if yes,
if size is greater than max, save that tree
"""


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        

def get_largest_bst(root: Node, max_bst_size: int = 0, max_bst: Node = None) -> tuple:
    # check if current root is bst and larger than current max
    temp_tree_size = get_tree_size(root)
    if is_bst(root) and temp_tree_size > max_bst_size:
        max_bst_size = temp_tree_size
        max_bst = root
    
    left_max_size, left_max = 0, None
    right_max_size, right_max = 0, None
    
    if root.left:
        left_max_size, left_max = get_largest_bst(root.left, max_bst_size, max_bst)
    if root.right:
        right_max_size, right_max = get_largest_bst(root.right, max_bst_size, max_bst)
        
    if left_max_size > max_bst_size and left_max_size > right_max_size:
        return left_max_size, left_max
    if right_max_size > max_bst_size and right_max_size > left_max_size:
        return right_max_size, right_max
    
    return max_bst_size, max_bst
            
        
        

def get_tree_size(node: Node, size: int = 0) -> int:
    size += 1
    if node.left and node.right:
        return get_tree_size(node.left, size) + get_tree_size(node.right, size) - size
    if node.left:
        return get_tree_size(node.left, size)
    if node.right:
        return get_tree_size(node.right, size)
    return size


def is_bst(node: Node) -> bool:
    if node.left and node.right:
        left_max = find_max_node(node.left)
        right_min = find_min_node(node.right)
        return left_max < node.value < right_min
    return False
            
    
def find_max_node(node: Node) -> int:
    if node.left and node.right:
        return max(node.value, find_max_node(node.left), find_max_node(node.right))
    if node.left:
        return max(node.value, find_max_node(node.left))
    if node.right:
        return max(node.value, find_max_node(node.right))
    return node.value


def find_min_node(node: Node) -> int:
    if node.left and node.right:
        return min(node.value, find_min_node(node.left), find_min_node(node.right))
    if node.left:
        return min(node.value, find_min_node(node.left))
    if node.right:
        return min(node.value, find_min_node(node.right))
    return node.value


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(5)), Node(3, Node(4, Node(6), Node(7, Node(3, Node(2))))))
    print(find_max_node(tree))
    print(find_min_node(tree))
    bst = Node(3, Node(1, Node(2)), Node(4, Node(5)))
    print(is_bst(bst))
    not_bst = Node(0, Node(1, Node(2)), Node(4, Node(5)))
    print(is_bst(not_bst))
    
    print(get_tree_size(tree))
    print(get_tree_size(bst))
    print(get_tree_size(not_bst))
    
    print(get_largest_bst(bst))
    """complex bst
             10
           /   \
          5     15
        /  \   /  \
       1    7 16   14
                  /  \
                 7    21
                / \   / \
               2  11 17  25
    """
    complex_bst = Node(10, Node(5, Node(1), Node(7)), Node(15, Node(16), Node(14, Node(7, Node(2), Node(11)), Node(21, Node(17), Node(25)))))
    get_largest_bst(complex_bst)