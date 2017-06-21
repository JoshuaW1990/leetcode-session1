# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        Use BFS search
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return result
        queue = [(0, root)]
        while queue:
            level, ptr = queue.pop(0)
            if ptr.left is not None:
                queue.append((level + 1, ptr.left))
            if ptr.right is not None:
                queue.append((level + 1, ptr.right))
            if len(result) == level:
                result.append([ptr.val])
            else:
                result[level] += [ptr.val]
        return result
