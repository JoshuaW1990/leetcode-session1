# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        In-order traversal of BST and compare the count of the current number with the maximum count

        :type root: TreeNode
        :rtype: List[int]
        """
        counter = dict()

        def inOrder(node):
            if node is None:
                return
            if node.val not in counter:
                counter[node.val] = 1
            else:
                counter[node.val] += 1
            inOrder(node.left)
            inOrder(node.right)

        inOrder(root)
        maxNum = max(counter.values() + [None])
        return [key for key in counter.keys() if counter[key] == maxNum]
