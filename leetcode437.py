"""
brute force search
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_path(self, root, sum):
        if not root:
            return 0
        num = self.find_path(root.left, sum - root.val) + self.find_path(root.right, sum - root.val)
        if root.val == sum:
            return 1 + num
        else:
            return num
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.find_path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

"""
Two sum solutions
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
