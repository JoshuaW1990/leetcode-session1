class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = None
        minDiff = float('inf')
        nums.sort()
        for i in xrange(len(nums) - 2):
            if i
