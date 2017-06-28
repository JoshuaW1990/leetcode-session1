# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        tail, current, prev = head, head, None
        while current.next:
            next = current.next
            current.next = prev
            prev = current
            current = next
        current.next = prev
        return current, tail

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = k
        ptr, prev = head, None
        while count > 0 and ptr:
            prev = ptr
            ptr = ptr.next
            count -= 1
        if count > 0:
            return head
        prev.next = None
        newHead, newTail = self.reverseList(head)
        newTail.next = self.reverseKGroup(ptr, k)
        return newHead
