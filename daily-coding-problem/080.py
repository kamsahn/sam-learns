"""
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""
    
# descend the root and count steps as you go
# save max depth
# do this recursively to get all branches


class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


class Store:
    def __init__(self, level: int = 0, node: Node = None):
        self.level = level
        self.node = node


def get_deepest_node(root: Node) -> Node:
    store = Store()
    
    def helper(node: Node, level: int, store: Store):
        if node.left or node.right:
            if node.left and node.right:
                helper(node.left, level+1, store)
                helper(node.right, level+1, store)
            if node.left:
                helper(node.left, level+1, store)
            if node.right:
                helper(node.right, level+1, store)
        else:
            if level > store.level:
                store.level = level
                store.node = node
    helper(root, 0, store)
    return store.node.value
        

if __name__ == "__main__":
    tree = Node("a", Node("b", Node("d")), Node("c"))
    print(get_deepest_node(tree))
    tree = Node("a", Node("b", Node("d"), Node("e", Node("f"), Node("g"))), Node("c", Node("h", Node("i", Node("je")))))
    print(get_deepest_node(tree))
