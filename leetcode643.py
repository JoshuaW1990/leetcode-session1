class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        tmpSum = sum(nums[:k])
        maxSum = tmpSum
        for i in xrange(len(nums) - k):
            j = i + k
            tmpSum = tmpSum - nums[i] + nums[j]
            maxSum = max(maxSum, tmpSum)
        return maxSum / float(k)
