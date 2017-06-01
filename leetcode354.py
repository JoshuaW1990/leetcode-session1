"""
https://discuss.leetcode.com/topic/48160/python-o-nlogn-o-n-solution-beats-97-with-explanation
"""
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def cmphelper(x, y):
            if x[0] < y[0] or (x[0] == y[0] and x[1] > y[1]):
                return -1
            else:
                return 1
        
        def lengthOfLIS(nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            DP = [[0, 0] for _ in nums]
            size = 0
            for item in nums:
                s, e = 0, size
                while s != e:
                    m = (s + e) / 2
                    if DP[m][1] >= item[1]:
                        e = m
                    else:
                        s = m + 1
                DP[s] = item
                size = max(s + 1, size)
            return size
        
        sort_envs = sorted(envelopes, cmp=cmphelper)
        return lengthOfLIS(sort_envs)