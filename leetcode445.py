# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Use stack
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        ptr1, ptr2 = l1, l2
        while ptr1 is not None:
            stack1.append(ptr1.val)
            ptr1 = ptr1.next
        while ptr2 is not None:
            stack2.append(ptr2.val)
            ptr2 = ptr2.next

        stack = []
        next_digit = 0
        while stack1 or stack2:
            if stack1:
                digit1 = stack1.pop()
            else:
                digit1 = 0
            if stack2:
                digit2 = stack2.pop()
            else:
                digit2 = 0
            digit = next_digit + digit1 + digit2
            next_digit = digit / 10
            digit %= 10
            stack.append(digit)
        if next_digit > 0:
            stack.append(next_digit)

        root = None
        while stack:
            digit = stack.pop()
            current_ptr = ListNode(digit)
            if root is None:
                root = current_ptr
            else:
                prev_ptr.next = current_ptr
            prev_ptr = current_ptr

        return root

        