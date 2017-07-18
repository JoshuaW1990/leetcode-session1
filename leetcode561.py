class Solution(object):
    def arrayPairSum(self, nums):
        """
        sort and get the sum of the subarray
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i in xrange(0, len(nums), 2):
            ans += nums[i]
        return ans
