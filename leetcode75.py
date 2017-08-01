"""
counting sort
two-pass
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1
        start = 0
        for i in xrange(3):
            size = counter[i]
            end = start + size
            nums[start:end] = [i] * size
            start = end


"""
one-pass
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p0, p2 = 0, len(nums) - 1
        index = 0
        while index <= p2:
            if nums[index] == 0:
                nums[index], nums[p0] = nums[p0], nums[index]
                p0 += 1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[p2] = nums[p2], nums[index]
                p2 -= 1
            else:
                index += 1
