"""
This is a solution that I'm pretty proud of. I got to the basic solution decently quickly, then ran into some issues
with edge cases. My final headache was not explicitly checking for None, but only looking checking for falsey values (in
the middle of the solution when checking if val l1 and l2 are integers).

I almost turned away from this due to my unfamiliarity with linked lists, but I'm glad I stuck around because this turned
into a fun challenge for me.
"""

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def get_val_remainder(self, val):
        """Return val and remainder. Check if > 10"""
        remainder = 0
        if val > 9:
            val -= 10
            remainder = 1
        return val, remainder

    def get_next_sum_link(self, next_l1, next_l2):
        return self.addTwoNumbers(next_l1, next_l2) if (next_l1 or next_l2) else None

    def get_next_link_remainder(self, link, remainder):
        return ListNode(val=link.next.val + remainder, next=link.next.next) if link.next else None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val_l1, val_l2 = None, None
        next_l1, next_l2 = None, None
        rem = 0  # remainder

        if l1:
            val_l1 = l1.val
        if l2:
            val_l2 = l2.val

        if val_l1 is not None and val_l2 is not None:
            sum_val = val_l1 + val_l2
        elif isinstance(val_l1, int):
            sum_val = val_l1
        elif isinstance(val_l2, int):
            sum_val = val_l2

        sum_val, rem = self.get_val_remainder(sum_val)

        if l1 and l2:
            if l1.next:
                next_l1 = self.get_next_link_remainder(l1, rem)
                next_l2 = self.get_next_link_remainder(l2, 0)
            else:
                next_l1 = self.get_next_link_remainder(l1, 0)
                next_l2 = self.get_next_link_remainder(l2, rem)
        elif l1:
            next_l1 = self.get_next_link_remainder(l1, rem)
        elif l2:
            next_l2 = self.get_next_link_remainder(l2, rem)

        if (not next_l1 and not next_l2) and rem:
            next_l1 = ListNode(val=rem, next=None)

        next_sum = self.get_next_sum_link(next_l1, next_l2)
        link_sum = ListNode(val=sum_val, next=next_sum)

        return link_sum
