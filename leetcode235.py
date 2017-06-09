# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def helper(root, node):
            """
            Helper function

            Search the node
            """
            if root is None:
                return []
            if root.val == node.val:
                return [root]
            elif root.val < node.val:
                return [root] + helper(root.right, node)
            else:
                return [root] + helper(root.left, node)
        p_ancestor = helper(root, p)
        q_ancestor = helper(root, q)
        minLength = min(len(p_ancestor), len(q_ancestor))
        for i in xrange(minLength):
            if p_ancestor[i] == q_ancestor[i]:
                continue
            else:
                return p_ancestor[i - 1].val
        return p_ancestor[minLength - 1].val



"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/#/description
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root

