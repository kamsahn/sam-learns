"""
A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node.
The following tree is an example:

       4
     / | \
   3   5   3
 /           \
9              9

        4
      / | \
    3   5   3
  /        /
9         9
Given a k-ary tree, determine whether it is symmetric.
"""


class Node:
    def __init__(self, k: int, value: int, children: list = None):
        self.k = k
        self.value = value
        if children:
            self.children = children
        else:
            self.children = [None for _ in range(k)]


def flip_tree(node: Node) -> Node:
    new_children = []   
    for child in node.children:
        if child:
            child = flip_tree(child)

        new_children.append(child)

    new_children.reverse()
    new_node = Node(node.k, node.value, new_children)
        
    return new_node


class Comparitor:
    def __init__(self):
        self.same = True
        
    def compare_trees(self, node1: Node, node2: Node):
        if node1.value == node2.value:
            for child1, child2 in zip(node1.children, node2.children):
                if child1 and child2:
                    self.compare_trees(child1, child2)
                else:
                    if child1 is not None and child2 is not None:
                        self.same = False
        else:
            self.same = False


def is_symmetric(node: Node) -> bool:
    flipped_node = flip_tree(node)
    c = Comparitor()
    c.compare_trees(node, flipped_node)
    return c.same
    

if __name__ == "__main__":
    k = 3
    tree = Node(k, 4, [Node(k, 3, [Node(k, 9), None, None]), Node(k, 5), Node(k, 3, [None, None, Node(k, 9)])])
    print(is_symmetric(tree))
    tree = Node(k, 4, [Node(k, 3, [Node(k, 8), None, None]), Node(k, 5), Node(k, 3, [None, None, Node(k, 9)])])
    print(is_symmetric(tree))
    tree = Node(k, 4, [Node(k, 3, [Node(k, 9), None, None]), Node(k, 5), Node(k, 3, [Node(k, 9), None, None])])
    print(is_symmetric(tree))
    tree = Node(k, 4, [Node(k, 3, [Node(k, 1), Node(k, 1), Node(k, 1)]), Node(k, 5), Node(k, 3, [Node(k, 2), Node(k, 2), Node(k, 2)])])
    print(is_symmetric(tree))
    
    k = 4
    tree = Node(k, 1, [Node(k, 2, [Node(k, 9), None, None, None]), Node(k, 3), Node(k, 3), Node(k, 2, [None, None, None, Node(k, 9)])])
    print(is_symmetric(tree))
    tree = Node(k, 1, [Node(k, 2, [Node(k, 9), None, None, None]), Node(k, 3), Node(k, 2, [None, None, None, Node(k, 9)]), Node(k, 3)])
    print(is_symmetric(tree))
