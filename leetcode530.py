# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxValue = -float('inf')
    minDiff = float('inf')

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.minDiff = min(self.minDiff, node.val - self.maxValue)
        self.maxValue = node.val
        self.helper(node.right)

    def getMinimumDifference(self, root):
        """
        traversal of BST
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.minDiff
