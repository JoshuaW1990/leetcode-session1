"""
DFS with stack: top down
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
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [(0, [], root)]
        result = []
        while stack:
            acc, tmp, ptr = stack.pop()
            if ptr.left:
                stack.append((acc + ptr.val, tmp + [ptr.val], ptr.left))
            if ptr.right:
                stack.append((acc + ptr.val, tmp + [ptr.val], ptr.right))
            if not ptr.left and not ptr.right and acc + ptr.val == sum:
                result.append(tmp + [ptr.val])
        return result


"""
DFS with recursion: bottom up
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
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if not root.left and not root.right:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        current = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + item for item in current]
