# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # http://www.cnblogs.com/zuoyuan/p/3701971.html
        dummy = ListNode(0)
        ptr1 = ptr2 = dummy
        dummy.next = head
        for i in xrange(n):
            ptr1 = ptr1.next
        while ptr1.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr2.next = ptr2.next.next
        return dummy.next
