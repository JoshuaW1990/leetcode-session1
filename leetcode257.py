# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []

        def helper(cur, node):
            if node.left is None and node.right is None:
                result.append(cur + [str(node.val)])
                return
            if node.left is not None:
                helper(cur + [str(node.val)], node.left)
            if node.right is not None:
                helper(cur + [str(node.val)], node.right)

        if root is None:
            return result
        helper([], root)
        for i, item in enumerate(result):
            result[i] = '->'.join(item)
        return result
