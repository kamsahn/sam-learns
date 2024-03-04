"""
Given a linked list of numbers and a pivot k,
partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.
"""

# go down the linked list and create two lists
# less than and equal-to-or-greater than
# attach at end


class LinkedNode:
    def __init__(self, value: int, tail=None):
        self.value = value
        self.tail = tail
    
    def end(self):
        if self.tail:
            return self.tail
        else:
            return self
    
    def pretty_print(self, display: str = ""):
        display += f"{self.value} -> "
        if self.tail:
            return self.tail.pretty_print(display)
        else:
            print(display[:-3])


def re_partition(node: LinkedNode, k: int, lesser: LinkedNode = None, greater: LinkedNode = None) -> LinkedNode:
    if node.value < k:
        if lesser:
            lesser.end().tail = LinkedNode(node.value)
        else:
            lesser = LinkedNode(node.value)
    else:
        if greater:
            greater.end().tail = LinkedNode(node.value)
        else:
            greater = LinkedNode(node.value)
    
    if node.tail:
        return re_partition(node.tail, k, lesser, greater)
    else:
        ans = lesser
        ans.end().tail = greater
        return ans


if __name__ == "__main__":
    ll = LinkedNode(5, LinkedNode(1, LinkedNode(8, LinkedNode(0, LinkedNode(3)))))
    ll.pretty_print()
    ans = re_partition(ll, 3)
    ans.pretty_print()
