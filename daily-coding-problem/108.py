"""
Print the nodes in a binary tree level-wise.
For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""
    
# traverse the node while writing to a dict
# dict key: level
# dict value: list of values
# go left first


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_tree_levels(tree: Node) -> None:
    print_dict = {}
    
    def print_tree_levels_helper(node: Node, level: int):
        if print_dict.get(level):
            print_dict[level].append(node.value)
        else:
            print_dict[level] = [node.value]
        if node.left:
            print_tree_levels_helper(node.left, level+1)
        if node.right:
            print_tree_levels_helper(node.right, level+1)
    
    print_tree_levels_helper(tree, 0)
    
    ans = ""
    for i in range(len(print_dict.keys())):
        for j in print_dict[i]:
            ans += ","+str(j)
    print(ans[1:])
    
    
if __name__ == "__main__":
    tree = Node(1, Node(2), Node(3, Node(4), Node(5)))
    print_tree_levels(tree)
    
    """
            1
           / \
          2   3
         / \   \
        4   5   6
       /   /   / \
      7   8   9   10
    """
    tree = Node(1, Node(2, Node(4, Node(7)), Node(5, Node(8))), Node(3, None, Node(6, Node(9), Node(10))))
    print_tree_levels(tree)
        
    