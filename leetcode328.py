# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddPtr = oddHead = ListNode(-1)
        evenPtr = evenHead = ListNode(-1)
        ptr = head
        while ptr:
            oddPtr.next = ptr
            oddPtr = oddPtr.next
            ptr = ptr.next
            if ptr:
                evenPtr.next = ptr
                evenPtr = evenPtr.next
                ptr = ptr.next
        oddPtr.next = evenHead.next
        evenPtr.next = None
        return oddHead.next
