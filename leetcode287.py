class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Hashmap: nums[n] = n + 1
        for i in xrange(len(nums)):
            digit = nums[i]
            while nums[digit - 1] != digit:
                nums[digit - 1], nums[i] = digit, nums[digit - 1]
                digit = nums[i]
        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                break
        return nums[i]
             

