"""
Given a binary tree, return the level of the tree with minimum sum.
"""

"""
level is a "horizontal" slice of the binary tree
traverse the tree (with recursion) and sum each level
return the min amount
"""
class Node:
    """
    Node class must have a value
    may have left and right references to other nodes
    """
    def __init__(self, value: int, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def get_min_level(tree: Node) -> int:
    """
    Return the int level with the lowest sum 
    root node being 0, incrementing each level down
    """
    # Create storage
    level_dict = {}
    level = 0

    # Define recursive function
    def get_min_level_helper(level: int, node: Node):
        if (level in level_dict):
            level_dict[level] = level_dict[level] + node.value
        else:
            level_dict[level] = node.value
        
        if node.left:
            get_min_level_helper(level + 1, node.left)
        if node.right:
            get_min_level_helper(level + 1, node.right)
        return

    # Call recursive function
    get_min_level_helper(level, tree)

    # Find lowest sum
    lowest = 9999 # arbitary high num
    ans_level = None
    for level, total in level_dict.items():
        if total < lowest:
            ans_level = level
    # ans_level = min(level_dict, key=level_dict.get) # fancy way to do above logic

    return ans_level

if __name__ == "__main__":
    tree = Node(4, Node(2, Node(1), Node(1)), Node(3, Node(1)))
    print(get_min_level(tree))

        
