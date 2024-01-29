"""
Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
"""

class Node:
    def __init__(self, value: int, tail = None):
        self.value = value
        self.tail = tail

def get_tail(node: Node):
    return get_tail(node.tail) if node.tail else node

def get_x_node(node: Node, x: int, i: int = 0) -> Node:
    return node if x == i else get_x_node(node.tail, x, i+1)
    

def rotate_linked_list(linked_list: Node, k: int) -> Node:
    k_node = get_x_node(linked_list, k)
    k_minus_one_node = get_x_node(linked_list, k-1)
    last_node = get_tail(linked_list)
    
    k_minus_one_node.tail = None
    last_node.tail = linked_list
    
    return k_node

def print_linked_list(linked_list: Node, ans: str = "") -> str:
    ans += str(linked_list.value)
    if linked_list.tail:
        ans += " -> "
        return print_linked_list(linked_list.tail, ans)
    else:
        return ans


if __name__ == "__main__":
    k = 2
    ll = Node(7, Node(7, Node(3, Node(5))))
    print(print_linked_list(ll))
    print("rotate by", k)
    print(print_linked_list(rotate_linked_list(ll, k)))
    print("")
    
    k = 3
    ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print(print_linked_list(ll))
    print("rotate by", k)
    print(print_linked_list(rotate_linked_list(ll, k)))
    print("")
