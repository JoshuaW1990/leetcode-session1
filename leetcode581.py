class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        sortNums = sorted(nums)
        start, end = None, None
        for i in xrange(len(nums)):
            if nums[i] != sortNums[i]:
                if start is None:
                    start = i
                else:
                    end = i
        if start is None:
            return 0
        else:
            return end - start + 1
