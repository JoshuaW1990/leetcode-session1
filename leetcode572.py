"""
Compare throught traversal of recursion
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, s, t):
        if s is None and t is None:
            return True
        elif (s is None) != (t is None):
            return False
        elif s.val != t.val:
            return False
        else:
            return self.helper(s.left, t.left) and self.helper(s.right, t.right)


    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None or t is None:
            return False
        return self.helper(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


"""
Compare through printing the string
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traversal(self, node):
        """
        traversal of pre-order
        """
        if node is None:
            return '$'
        return '^' + str(node.val)  + '#' + self.traversal(node.left) + '#' + self.traversal(node.right)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.traversal(t) in self.traversal(s)
