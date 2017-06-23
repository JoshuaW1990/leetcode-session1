# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getHeight(self, node):
        if node:
            return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        else:
            return 0

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1
            else:
                return False
        else:
            return True
