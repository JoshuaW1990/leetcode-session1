class Solution(object):
    def helper(self, wealths):
        print wealths
        dp = [0 for _ in xrange(1 + len(wealths))]
        dp[0] = 0
        dp[1] = wealths[0]
        for i in xrange(1, len(wealths)):
            num = wealths[i]
            dp[i + 1] = max(dp[i], dp[i - 1] + num)
        print "dp: ", dp
        return dp[-1]


    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print nums
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        max1 = self.helper([0] + nums[1:])
        max2 = self.helper(nums[:-1] + [0])
        return max(max1, max2)
        