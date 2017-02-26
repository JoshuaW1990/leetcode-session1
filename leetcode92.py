# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in xrange(1, m): 
            pre = pre.next
        
        start, then = pre.next, pre.next.next
        for i in xrange(n - m):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        return dummy.next
        
                
