"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.

Implement locking in a binary tree.
A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like.
You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes.
Each method should run in O(h), where h is the height of the tree.
"""

"""
Example tree:
         1
       /
      2
     / \
    3   4
      /  \
     5    6
"""

class Node():
    def __init__(self, val, left=None, right=None):
        """
        :param val: int, value of node
        :param left: Node, left node
        :param right: Node, right node
        """
        self.val = val
        self.left = left
        self.right = right
        self.parent = None
        self.is_locked = False

        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def lock(self):
        """attempts to lock node if all descendants or ancestors are unlocked"""
        if self.check_ancestors_unlocked() and self.check_descendants_unlocked():
            self.is_locked = True
        else:
            print('Could not unlock. Not all descendants AND ancestors are unlocked.')

    def unlock(self):
        """attemps to unlock node if all descendants or ancestors are unlocked"""
        if self.check_ancestors_unlocked() and self.check_descendants_unlocked():
            self.is_locked = False
        else:
            print('Could not unlock. Not all descendants AND ancestors are unlocked.')

    def check_descendants_unlocked(self):
        """walk down tree and check if unlocked"""
        if self.left:
            if not self.left.is_locked:
                if not self.left.check_descendants_unlocked():
                    return False
            else:
                return False
        if self.right:
            if not self.right.is_locked:
                if not self.right.check_descendants_unlocked():
                    return False
            else:
                return False
        return True

    def check_ancestors_unlocked(self):
        """walk up tree and check if unlocked"""
        if self.parent:
            if self.parent.is_locked:
                return False
            if not self.parent.check_ancestors_unlocked():
                return False
        return True

# example tree
six = Node(6, None, None)
five = Node(5, None, None)
four = Node(4, five, six)
three = Node(3, None, None)
two = Node(2, three, four)
one = Node(1, two, None)


print('locking four', four.lock())
print('is four locked?', four.is_locked)
print('locking five', five.lock())
print('is five locked?', five.is_locked)
print('unlocking four', four.unlock())
print('is four locked?', four.is_locked)
print('locking five', five.lock())
print('is five locked?', five.is_locked)

