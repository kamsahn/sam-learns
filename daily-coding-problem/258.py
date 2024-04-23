"""
In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7].
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def boustrophedon(tree: Node) -> list[int]:
    def helper(queue: list[Node], level=1, ans=[]):
        if len(queue) == 0:
            return ans
        new_queue = []
        if level % 2 == 0:
            for node in queue:
                ans.append(node.val)
                if node.right:
                    new_queue.append(node.right)
                if node.left:
                    new_queue.append(node.left)
        else:
            for node in queue:
                ans.append(node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)

        new_queue.reverse()
        return helper(new_queue, level + 1, ans)
    
    queue = []
    if tree.right:
        queue.append(tree.right)
    if tree.left:
        queue.append(tree.left)
    
    return helper(queue, 2, [tree.val])


if __name__ == "__main__":
    tree = Node(1,
                Node(2, Node(4, Node(8), Node(9)), Node(5, Node(10), Node(11))),
                Node(3, Node(6, Node(12), Node(13)), Node(7, Node(14), Node(15)))
                )
    print(boustrophedon(tree))
    tree = Node(1,
                Node(2, Node(4, Node(7), Node(8))),
                Node(3, Node(5, Node(9), Node(10)), Node(6, Node(11), Node(12)))
                )
    print(boustrophedon(tree))
