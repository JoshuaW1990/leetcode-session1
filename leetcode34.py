class Solution(object):
    def binarySearch(self, nums, target):
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # binary search
        if len(nums) == 0:
            return [-1, -1]
        startIndex = self.binarySearch(nums, target - 0.5)
        endIndex = self.binarySearch(nums, target + 0.5)
        if nums[startIndex] < target:
            startIndex += 1
        if nums[endIndex] > target:
            endIndex -= 1
        if startIndex > endIndex:
            return [-1, -1]
        else:
            return [startIndex, endIndex]
