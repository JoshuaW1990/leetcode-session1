# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def helper(shortList, longList, counterPtr):
            ptrShort, ptrLong = shortList, longList
            while counterPtr:
                counterPtr = counterPtr.next
                ptrLong = ptrLong.next
            while ptrShort != ptrLong:
                ptrShort = ptrShort.next
                ptrLong = ptrLong.next
            return ptrShort

        ptrA, ptrB = headA, headB
        while ptrA and ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next
        if ptrA is not None:
            ans = helper(headB, headA, ptrA)
        else:
            ans = helper(headA, headB, ptrB)
        return ans
