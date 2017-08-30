class Solution(object):
    def binarySearch(self, nums, target):
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # binary search
        index = self.binarySearch(nums, target)
        if index == -1:
            return [-1, -1]
        start = end = index
        while start >= 0:
            if nums[start] != target:
                start += 1
                break
            start -= 1
        while end < len(nums):
            if nums[end] != target:
                end -= 1
                break
            end += 1
        return [start, end]
