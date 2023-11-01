"""
Determine whether a doubly linked list is a palindrome.
What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True
while 1 -> 4 returns False
"""

class DoubleLink:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def set_left(self, left):
        self.left = left
        
    def set_right(self, right):
        self.right = right

class LinkedList:
    def __init__(self, start: DoubleLink):
        def get_length(node: DoubleLink, length: int=0) -> int:
            length += 1
            if node.right:
                return get_length(node.right, length)
            else:
                return length
        
        def get_end(node: DoubleLink) -> DoubleLink:
            if node.right:
                return get_end(node.right)
            else:
                return node
            
        self.start = start
        self.end = get_end(start)
        self.length = get_length(start)
            
# list helpers:

def set_left(link1: DoubleLink, link2:DoubleLink):
    link1.set_left(link2)
    link2.set_right(link1)
    
def set_right(link1: DoubleLink, link2:DoubleLink):
    link1.set_right(link2)
    link2.set_left(link1)

def read_list(linked_list: LinkedList):
    def read_list_helper(node: DoubleLink, ans: str):
        ans += str(node.value)
        if node.right:
            ans += " -> "
            read_list_helper(node.right, ans)
        else:
            print(ans)
    read_list_helper(linked_list.start, "")
    
def define_list(*vals: int) -> LinkedList:
    node = None
    last_node = None
    for val in vals:
        if not node:
            node = DoubleLink(val)
            last_node = node
        else:
            temp_node = DoubleLink(val)
            set_right(last_node, temp_node)
            last_node = temp_node
    return LinkedList(node)

def is_palindrome(linked_list: LinkedList) -> bool:
    """
    Gets length of linked list
    checks ends of list and walks inwards, ensuring all values are equal
    """
    length = linked_list.length
    start = linked_list.start
    end = linked_list.end
    
    # if singly linked, need to make a function to access index [length - i]
    
    for i in range(length):
        if start == end:
            return True
        if start.value != end.value:
            return False
        if i > length/2:
            return True
        start = start.right
        end = end.left
        
        

    
if __name__ == "__main__":
    dlist = define_list(1,4,3,4,1)
    read_list(dlist)
    print(is_palindrome(dlist))
    dlist = define_list(1,4,3,4)
    read_list(dlist)
    print(is_palindrome(dlist))
    dlist = define_list(1,4)
    read_list(dlist)
    print(is_palindrome(dlist))
    dlist = define_list(1,4,4,1)
    read_list(dlist)
    print(is_palindrome(dlist))
    dlist = define_list(1,4,4,3,1)
    read_list(dlist)
    print(is_palindrome(dlist))
    