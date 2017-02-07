class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Utilize the bit operation
        # https://discuss.leetcode.com/topic/17629/the-simplest-solution-ever-with-clear-explanation/2
        b1, b0 = 0, 0
        for num in nums:
            b0 = (b0 ^ num) & (~b1)
            b1 = (b1 ^ num) & (~b0)
        return b0
