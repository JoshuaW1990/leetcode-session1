class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Hash table
        bucket = len(nums)
        for i in xrange(len(nums)):
            idx = nums[i]
            while idx != i:
                if i >= bucket and idx == i + 1:
                    break
                if idx == bucket:
                    idx -= 1
                    bucket -= 1
                tmp = nums[idx]
                nums[idx] = nums[i]
                nums[i] = tmp
                idx = nums[i]
        return bucket

        # use bit manipulation
        result = 0
        for i in xrange(len(nums) + 1):
            result ^= i
        for num in nums:
            result ^= num
        return result
            
        
