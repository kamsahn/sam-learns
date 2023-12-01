"""
Given k sorted singly linked lists,
write a function to merge all the lists into one sorted singly linked list.
"""

# sort all lists by head value
# for each list:
# if tail value n < head value n+1, attach lists tail to head
# if tail value n > head value n+1, break down both lists and merge values individually and recreate a new list


class LinkedList:
    def __init__(self, value: int, tail = None):
        self.value = value
        self.tail = tail
        

def get_tail(node: LinkedList):
    if node.tail:
        return get_tail(node.tail)
    else:
        return node


def list_generator(values: list) -> LinkedList:
    values.sort()
    ans = None
    for value in values:
        if ans:
            tail = get_tail(ans)
            tail.tail = LinkedList(value)
        else:
            ans = LinkedList(value)
    
    return ans


def list_separator(linked_list: LinkedList) -> list:
    ans = []
    node = linked_list
    while node:
        ans.append(node.value)
        node = node.tail
    return ans


def get_single_list(lists: list) -> LinkedList:
    heads = [(linked_list.value, linked_list) for linked_list in lists]
    heads.sort(key=lambda x: x[0])
    
    ans = heads[0][1]
    
    for i in range(len(heads)):
        if i+1 < len(heads):
            next_ans = heads[i+1][1]
            ans_tail = get_tail(ans)
            
            if ans_tail.value > next_ans.value:
                ans = list_generator(
                    list_separator(ans) + list_separator(next_ans)
                )
            else:
                get_tail(ans).tail = next_ans
            
    return ans
        

if __name__ == "__main__":
    k = [
        list_generator([2, 3, 4]),
        list_generator([6, 7, 8, 9]),
        list_generator([1, 2, 2]),
        list_generator([7, 8, 9])
    ]
    a = get_single_list(k)
    print(list_separator(a))
    