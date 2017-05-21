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
        prev, ptr = head, head.next
        while ptr is not None:
            if prev.val == ptr.val:
                ptr = ptr.next
            else:
                prev.next = ptr
                prev = prev.next
                ptr = ptr.next
        prev.next = None
        return head
