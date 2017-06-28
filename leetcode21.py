# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        ptr1, ptr2 = l1, l2
        head = ListNode(0)
        current = head
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next
            current = current.next
        if ptr1 is None:
            current.next = ptr2
        else:
            current.next = ptr1
        return head.next
