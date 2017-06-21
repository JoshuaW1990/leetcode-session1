# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        Use the BFS with two queues. The only difference is the direction of the childs is different
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        queue1, queue2 = [root], [root]
        while queue1 and queue2:
            ptr1 = queue1.pop(0)
            ptr2 = queue2.pop(0)
            if ptr1 is not None and ptr2 is not None:
                if ptr1.val != ptr2.val:
                    return False
                else:
                    queue1.append(ptr1.left)
                    queue1.append(ptr1.right)
                    queue2.append(ptr2.right)
                    queue2.append(ptr2.left)
            elif ptr1 is None and ptr2 is None:
                continue
            else:
                return False
        return True
