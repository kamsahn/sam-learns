"""
Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""


class LinkedNode:
    def __init__(self, value: int, tail = None):
        self.value = value
        self.tail = tail


def swap(linked_list: LinkedNode) -> LinkedNode:
    def swap_helper(linked_node: LinkedNode):
        head, tail = linked_node.value, linked_node.tail.value
        linked_node.value = tail
        linked_node.tail.value = head
        if linked_node.tail.tail and linked_node.tail.tail.tail:
            swap_helper(linked_node.tail.tail)

    swap_helper(linked_list)
    return linked_list
    

if __name__ == "__main__":
    ll = LinkedNode(1, LinkedNode(2, LinkedNode(3, LinkedNode(4))))
    print(ll.value, "->", ll.tail.value, "->", ll.tail.tail.value, "->", ll.tail.tail.tail.value)
    swap(ll)
    print(ll.value, "->", ll.tail.value, "->", ll.tail.tail.value, "->", ll.tail.tail.tail.value)
    
    ll = LinkedNode(1, LinkedNode(2, LinkedNode(3, LinkedNode(4, LinkedNode(5)))))
    print(ll.value, "->", ll.tail.value, "->", ll.tail.tail.value, "->", ll.tail.tail.tail.value, "->", ll.tail.tail.tail.tail.value)
    swap(ll)
    print(ll.value, "->", ll.tail.value, "->", ll.tail.tail.value, "->", ll.tail.tail.tail.value, "->", ll.tail.tail.tail.tail.value)
    