# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        ptr, prev = head, None
        small_head, big_head = ListNode(0), ListNode(0)
        small_tail, big_tail = small_head, big_head
        while ptr:
            if ptr.val < x:
                small_tail.next = ptr
                small_tail = ptr
            else:
                big_tail.next = ptr
                big_tail = ptr
            ptr = ptr.next
        big_tail.next = None
        small_tail.next = big_head.next
        head = small_head.next
        return head
        
