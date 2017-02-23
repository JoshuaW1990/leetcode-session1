# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        queue = [root]
        while queue != []:
            ptr = queue[0]
            del queue[0]
            ptr.left, ptr.right = ptr.right, ptr.left
            if ptr.left is not None:
                queue.append(ptr.left)
            if ptr.right is not None:
                queue.append(ptr.right)
        return root
