class Solution(object):
    def binarySearch(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 1. use binary search to divide the array into two parts
        # 2. search according to the value of the target in the specific parts
        start, end = 0, len(nums) - 1
        while start < end - 1:
            mid = (start + end) / 2
            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[end]:
                end = mid
        prev = nums[:end]
        next = nums[end:]
        if len(prev) > 0 and prev[0] <= target <= prev[-1]:
            return self.binarySearch(prev, target)
        else:
            index = self.binarySearch(next, target)
            if index == -1:
                return -1
            else:
                return len(prev) + index
