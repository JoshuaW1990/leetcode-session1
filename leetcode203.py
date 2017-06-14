# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head is not None and head.val == val:
            head = head.next

        ptr = head
        prev = None
        while ptr:
            while ptr is not None and ptr.val == val:
                ptr = ptr.next
            if prev is not None:
                prev.next = ptr
            if ptr is not None:
                prev = ptr
                ptr = ptr.next
        return head