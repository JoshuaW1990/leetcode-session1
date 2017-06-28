"""
Switch values of node
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        if not ptr:
            return None
        while ptr.next:
            prev = ptr
            ptr = ptr.next
            prev.val, ptr.val = ptr.val, prev.val
            if ptr.next:
                ptr = ptr.next
            else:
                break
        return head


"""
Switch the nodes: recursion
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = head
        next = head.next
        ptr = next.next
        next.next = prev
        prev.next = self.swapPairs(ptr)
        return next
