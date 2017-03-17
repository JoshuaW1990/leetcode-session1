class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        """
        This solution is inspired by StefanPochmann.
        https://discuss.leetcode.com/topic/35494/solution-explanation
        """
        miss, add, index = 1, 0, 0
        while index <= n:
            if index < len(nums) and nums[index] <= miss:
                miss += nums[index]
                index += 1
            else:
                miss += miss
                add += 1
        return add
