"""
1. sort the list
2. run LCS
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = list(set(nums))
        sort_nums.sort()   
        return self.lengthOfLCS(nums, sort_nums)
    
    def lengthOfLCS(self, nums1, nums2):
        """
        Use DP and memoization for LCS
        """
        DP = [[0 for i in xrange(len(nums2) + 1)] for j in xrange(len(nums1) + 1)]
        for i in xrange(1, len(nums1) + 1):
            for j in xrange(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    DP[i][j] = DP[i - 1][j - 1] + 1
                else:
                    DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
        return DP[-1][-1]


"""
Run an LIS algorithm
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        DP = [1 for _ in xrange(len(nums))]
        for i in xrange(1, len(nums)):
            maxDP = 0
            for j in xrange(i):
                if nums[j] >= nums[i]:
                    continue
                maxDP = max(maxDP, DP[j])
            DP[i] = maxDP + 1
        return max(DP)


"""
Binary search
https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size