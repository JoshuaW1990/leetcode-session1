class Solution(object):
    def twoSum(self, nums, target):
        """
        Use the naive solution: search in two loop

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        counter = dict()
        for i in xrange(n):
            if nums[i] in counter:
                return [counter[nums[i]], i]
            else:
                counter[target - nums[i]] = i
