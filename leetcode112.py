# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        Use DFS algorithm: stack
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        stack = [(0, root)]
        while stack:
            acc, ptr = stack.pop()
            if ptr.left is not None:
                stack.append((acc + ptr.val, ptr.left))
            if ptr.right is not None:
                stack.append((acc + ptr.val, ptr.right))
            if ptr.left is None and ptr.right is None:
                if acc + ptr.val == sum:
                    return True
        return False


"""
https://discuss.leetcode.com/topic/10524/short-python-recursive-solution-o-n
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
