class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Hashmap: nums[n] = n + 1
        # The problem is that the array is not allowed to be modified
        # for i in xrange(len(nums)):
        #     digit = nums[i]
        #     while nums[digit - 1] != digit:
        #         nums[digit - 1], nums[i] = digit, nums[digit - 1]
        #         digit = nums[i]
        # for i in xrange(len(nums)):
        #     if nums[i] != i + 1:
        #         break
        # return nums[i]
        low = 0
        high = len(nums) - 1
        mid = (high + low) / 2
        while low < high - 1:
            mid = (high + low) / 2
            count = 0
            for num in nums:
                if mid < num <= high:
                    count += 1
            if count > high - mid:
                low = mid
            else:
                high = mid
        return high



             

