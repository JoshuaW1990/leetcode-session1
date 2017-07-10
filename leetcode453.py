class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minNum = min(nums)
        ans = 0
        for num in nums:
            ans += num - minNum
        return ans
