class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        counter = dict()
        for i in xrange(n):
            if nums[i] in counter:
                return [counter[nums[i]] + 1, i + 1]
            else:
                counter[target - nums[i]] = i
