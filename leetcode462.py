class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        sort_nums = sorted(nums)
        mid = len(nums) / 2
        target_num = sort_nums[mid]
        result = 0
        for num in sort_nums:
            result += abs(num - target_num)
        return result
        
        