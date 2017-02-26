class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            num = nums[i]
            nums[abs(num) - 1] = - abs(nums[abs(num) - 1])
        result = []
        for i in xrange(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result
