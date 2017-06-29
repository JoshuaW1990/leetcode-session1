# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        if t.left is not None and t.right is not None:
            result = '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
        elif t.left is not None:
            result = '(' + self.tree2str(t.left) + ')'
        elif t.right is not None:
            result = '()' + '(' + self.tree2str(t.right) + ')'
        else:
            result = ''
        return str(t.val) + result