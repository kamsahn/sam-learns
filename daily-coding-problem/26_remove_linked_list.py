"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

# as you walk down the list, keep track of the kth, kth -1 and kth+1 last element and change as you go

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def remove_k(self, k):
        count = 0
        kth = None
        kthminus1 = None
        kthplus1 = None
        if self.head:
            current = self.head
            count += 1
            while current.next:
                current = current.next
                count += 1
                if count > k:
                    if not kth:
                        kth = self.head
                        kthplus1 = kth.next
                    else:
                        kthminus1 = kth
                        kth = kthminus1.next
                        kthplus1 = kth.next
            # current.next == None
            # remove kth from the list
            kthminus1.next = kthplus1
            return kth
        else:
            raise

    def count(self):
        count = 0
        if self.head:
            count += 1
            current = self.head
            while current.next:
                current = current.next
                count += 1
        return count



l1 = LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)
l1.insert(6)

print(l1.count())
print(l1.remove_k(3).val)
print(l1.count())
