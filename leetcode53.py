class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[-float('inf'), -float('inf')] for _ in xrange(len(nums) + 1)]
        dp[0] = [0, 0]
        maxNum = -float('inf')
        for i, num in enumerate(nums):
            index = i + 1
            dp[index] = [min(dp[i]), dp[i][1] + num]
            if dp[index][1] - dp[index][0] > maxNum:
                maxNum = dp[index][1] - dp[index][0]
        return maxNum


"""
https://discuss.leetcode.com/topic/10722/a-python-solution/2
"""
class Solution(object):
    def maxSubArray(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
