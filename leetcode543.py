# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node):
        if node is None:
            return 0, 0
        leftDepth, leftDiameter = self.helper(node.left)
        rightDepth, rightDiameter = self.helper(node.right)
        diameter = max([leftDiameter, rightDiameter, leftDepth + rightDepth])
        return max(leftDepth, rightDepth) + 1, diameter



    def diameterOfBinaryTree(self, root):
        """
        Use recursive
        :type root: TreeNode
        :rtype: int
        """
        depth, diameter = self.helper(root)
        return diameter
