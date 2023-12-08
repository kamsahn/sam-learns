"""
Given the head of a singly linked list, reverse it in-place.
"""


class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value
        self.tail = tail
        

def print_linked_list(linked_list: LinkedNode, ans = []):
    ans.append(linked_list.value)
    if linked_list.tail:
        print_linked_list(linked_list.tail, ans)
    else:
        print(ans)
    
    
def reverse_linked_list(linked_list: LinkedNode, ans: LinkedNode = None) -> LinkedNode:
    def get_tail(node: LinkedNode) -> LinkedNode:
        return get_tail(node.tail) if node.tail else node
    
    def delete_tail(node: LinkedNode):
        if node.tail.tail:
            delete_tail(node.tail)
        else:
            node.tail = None
    
    tail_node = get_tail(linked_list)
    if tail_node:
        if ans:
            ans.tail = tail_node
        else:
            ans = LinkedNode(tail_node)
        
        delete_tail(linked_list)
        return reverse_linked_list(linked_list, ans)
    else:
        return ans


if __name__ == "__main__":
    ll = LinkedNode(1, LinkedNode(2, LinkedNode(3, LinkedNode(4))))
    print_linked_list(reverse_linked_list(ll))
