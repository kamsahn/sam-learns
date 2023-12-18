"""
Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

 10
/  \
5    5
 \     \
  2    1
 /
-1
"""

class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        

def min_path(node: Node, path: list[int]) -> list[int]:
    if node.left and node.right:
        path_left = [n for n in path]
        path_left.append(node.left.value)
        min_path_left = min_path(node.left, path_left)
        path_right = [n for n in path]
        path_right.append(node.right.value)
        min_path_right = min_path(node.right, path_right)
        
        if sum(min_path_left) < sum(min_path_right):
            return min_path_left
        else:
            return min_path_right
    elif node.left:
        path.append(node.left.value)
        return min_path(node.left, path)
    elif node.right:
        path.append(node.right.value)
        return min_path(node.right, path)
    else:
        return path
    

if __name__ == "__main__":
    tree = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1))))
    print(min_path(tree, [tree.value]))
