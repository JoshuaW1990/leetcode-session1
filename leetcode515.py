# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Naive solutions:
Use the bfs search. In the queue for BFS, each item is composed by a tuple: (rowIndex, node)
"""

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        queue = [(0, root)]
        prevRow = 0
        result = []
        maxNum = -float('inf')
        while queue:
            rowIndex, node = queue[0]
            if rowIndex != prevRow:
                result.append(maxNum)
                maxNum = -float('inf')
                prevRow += 1
            else:
                if maxNum < node.val:
                    maxNum = node.val
                if node.left is not None:
                    queue.append((rowIndex+1, node.left))
                if node.right is not None:
                    queue.append((rowIndex+1, node.right))
                del queue[0]
        result.append(maxNum)
        return result