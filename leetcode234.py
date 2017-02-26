# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Naive solution: don't consider the O(n) time and O(1) space
        # use a list to store value in the linked list and run from the two sides to the middle of the list.
        if head is None:
            return True
        values = []
        ptr = head
        while ptr is not None:
            values.append(ptr.val)
            ptr = ptr.next
        start = 0
        end = len(values) - 1
        while start < end:
            if values[start] == values[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
        # Improved solutions: Considering the O(n) time and O(1) space
        # Use the fast-slow pointer method to find the middle bucket of the linked list. Then reverse the half of the linked list. Finally compare these two parts one by one.
        def reverseList(ptr):
            if ptr is None:
                return None
            first = ptr
            if first.next is None:
                return first
            rest = reverseList(first.next)
            first.next.next = first
            first.next = None
            return rest

        slow, fast = head, head
        if head is None or head.next is None:
            return True
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        reverseHead = reverseList(slow)
        ptr1 = head
        ptr2 = reverseHead
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val != ptr2.val:
                return False
            else:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
        return True
