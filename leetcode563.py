# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    self.result = 0
    def findSum(self, current_root):
        """
        Calculate the sum of the tree whose root is current_root and edit the result by calculating on the fly to avoid unecessary traversal
        """
        if current_root is None:
            return 0
        left_sum = self.findSum(current_root.left)
        right_sum = self.findSum(current_root.right)
        self.result += abs(left_sum - right_sum)
        return current_root.val + left_sum + right_sum

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.findSum(root)
        return self.result
