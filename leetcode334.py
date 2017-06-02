"""
First sessions
"""

"""
Naive solution: O(n^3) time complexity
This solution will cause time limit exceeded
"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        for i in xrange(length):
            for j in xrange(i + 1, length):
                for k in xrange(j + 1, length):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False

"""
Advanced solution:
https://discuss.leetcode.com/topic/39807/python-easy-o-n-solution
"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = float('inf'), float('inf')
        for item in nums:
            if item <= first:
                first = item
            elif item <= second:
                second = item
            else:
                return True
        return False


        