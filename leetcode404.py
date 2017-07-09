# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        Traversal with stack or queue
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = [(root, 'right')]
        ans = 0
        while queue:
            node, pos = queue.pop(0)
            if node.left is None and node.right is None and pos == 'left':
                ans += node.val
            if node.left is not None:
                queue.append((node.left, 'left'))
            if node.right is not None:
                queue.append((node.right, 'right'))
        return ans
