# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # iterative method
        if head is None or head.next is None:
            return head
        current, prev = head.next, head
        prev.next = None
        while current is not None:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev
        # recursive method
        if head is None or head.next is None:
            return head
        first = head
        rest = self.reverseList(first.next)
        first.next.next = first
        first.next = None
        return rest
        
        
        
        
