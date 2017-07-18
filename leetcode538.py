# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    nodeValues = 0
    def helper(self, root):
        if root is None:
            return
        if root.right is not None:
            self.convertBST(root.right)
        self.nodeValues += root.val
        root.val = self.nodeValues
        if root.left is not None:
            self.convertBST(root.left)

    def convertBST(self, root):
        """
        Tree traversal from right to left
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root)
        return root
