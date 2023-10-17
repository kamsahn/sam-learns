"""
Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
"""

"""
method should take pick from a range (finite) of numbers and create that many nodes in one operation
"""
import random


class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def get_size(self):
        left_size = self.left.get_size() if self.left else 0
        right_size = self.right.get_size() if self.right else 0
        return 1 + left_size + right_size


def generate() -> Node:
    def tree_builder(
            node: Node,
            probability_add_children: float = 0.9,
            probability_add_branch: float = 0.9) -> None:
        if random.random() > probability_add_children:
            return
        if random.random() < probability_add_branch:
            node.left = Node(random.randint(1, 1000))
            return tree_builder(node.left, probability_add_children, probability_add_branch)
        if random.random() < probability_add_branch:
            node.right = Node(random.randint(1, 1000))
            return tree_builder(node.right, probability_add_children, probability_add_branch)
    tree = Node(random.randint(1, 1000))
    tree_builder(tree)
    return tree
        

if __name__ == "__main__":
    print(generate().get_size())
    