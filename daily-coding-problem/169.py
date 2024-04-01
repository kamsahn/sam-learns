"""
Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""


class LinkedNode:
    def __init__(self, value: int, tail=None):
        self.value = value
        self.tail = tail
    
    def get_tail(self):
        return self if not self.tail else self.tail.get_tail()
    
    def pretty_print(self, pp: str = ""):
        pp += f"{self.value} -> "
        if self.tail:
            self.tail.pretty_print(pp)
        else:
            print(pp[:-4])
    

def sort_linked_list(linked_list: LinkedNode) -> LinkedNode:
    low = linked_list
    curr = linked_list
    prev = None
    
    while curr:
        if low.value >= curr.value:
            temp = low
            low = curr
            if prev:
                prev.tail = curr.tail
            else:
                curr.tail = curr.tail.tail
                
            low.tail = temp
        
        prev = curr
        curr = curr.tail
    
    return low


if __name__ == "__main__":
    ll = LinkedNode(4, LinkedNode(1, LinkedNode(-3, LinkedNode(99))))
    ans = sort_linked_list(ll)
    ans.pretty_print()
    
    ll = LinkedNode(4, LinkedNode(3, LinkedNode(2, LinkedNode(1, LinkedNode(0)))))
    ans = sort_linked_list(ll)
    ans.pretty_print()
    
    ll = LinkedNode(0, LinkedNode(3, LinkedNode(2, LinkedNode(1, LinkedNode(4)))))
    ans = sort_linked_list(ll)
    ans.pretty_print()
    
    ll = LinkedNode(0, LinkedNode(3, LinkedNode(2, LinkedNode(1, LinkedNode(0)))))
    ans = sort_linked_list(ll)
    ans.pretty_print()
    
    ll = LinkedNode(1, LinkedNode(2, LinkedNode(3, LinkedNode(4, LinkedNode(0)))))
    ans = sort_linked_list(ll)
    ans.pretty_print()
    
    ll = LinkedNode(4, LinkedNode(4, LinkedNode(4, LinkedNode(4, LinkedNode(4)))))
    ans = sort_linked_list(ll)
    ans.pretty_print()
    
    ll = LinkedNode(4, LinkedNode(4, LinkedNode(4, LinkedNode(4, LinkedNode(0)))))
    ans = sort_linked_list(ll)
    ans.pretty_print()
