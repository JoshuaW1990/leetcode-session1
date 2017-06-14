# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        prev_ptr = None
        next_digit = 0
        while ptr1 is not None or ptr2 is not None:
            if ptr1 is not None:
                digit1 = ptr1.val
                ptr1 = ptr1.next
            else:
                digit1 = 0

            if ptr2 is not None:
                digit2 = ptr2.val
                ptr2 = ptr2.next
            else:
                digit2 = 0

            current_ptr = ListNode(digit1 + digit2 + next_digit)
            next_digit = current_ptr.val / 10
            current_ptr.val %= 10
            if prev_ptr is not None:
                prev_ptr.next = current_ptr
            else:
                root = current_ptr
            prev_ptr = current_ptr
        if next_digit == 1:
            current_ptr = ListNode(1)
            prev_ptr.next = current_ptr
        return root