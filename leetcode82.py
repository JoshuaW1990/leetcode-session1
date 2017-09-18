# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy = ListNode(-1)
        parentNode = dummy
        prev = None
        current = head
        next = current.next
        while next:
            if (prev is None and current.val != next.val) or (prev is not None and prev.val != current.val != next.val):
                parentNode.next = current
                parentNode = parentNode.next
            prev = current
            current = next
            next = current.next
        if prev is None or current.val != prev.val:
            parentNode.next = current
            parentNode = parentNode.next
        parentNode.next = None
        return dummy.next
