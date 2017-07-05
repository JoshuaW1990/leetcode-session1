class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [0 for _ in xrange(len(nums) + 1)]
        dp[0] = 0
        dp[1] = nums[0]
        for i in xrange(1, len(nums)):
            num = nums[i]
            dp[i + 1] = max(dp[i], dp[i - 1] + num)
        return dp[-1]