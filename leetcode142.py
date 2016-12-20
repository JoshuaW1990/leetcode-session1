# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Use set
        visited = set()
        ptr = head
        while ptr is not None:
            if ptr in visited:
                return ptr
            else:
                visited.add(ptr)
                ptr = ptr.next
        return None
        # Use two pointers
        if head is None or head.next is None:
            return None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                fast = fast.next
                slow = slow.next
            return fast
        return None