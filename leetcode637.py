# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = [(root, 0)]
        count = dict()
        ans = []
        while queue:
            node, level = queue.pop(0)
            if level not in count:
                count[level] = [node.val]
            else:
                count[level].append(node.val)
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        index = 0
        while index in count:
            total = sum(count[index])
            length = len(count[index])
            ans.append(total / float(length))
            index += 1
        return ans
