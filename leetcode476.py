"""
https://discuss.leetcode.com/topic/74611/simple-python
"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num



"""
https://discuss.leetcode.com/topic/74897/maybe-fewest-operations
"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = num
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return mask ^ num
