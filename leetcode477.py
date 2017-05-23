"""
Naive Solution: 
call hammingDistance function and compare each pair one by one
result: time limited exceeded
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        stringX = format(x, 'b').zfill(32)
        stringY = format(y, 'b').zfill(32)
        distance = 0
        for i, chX in enumerate(stringX):
            chY = stringY[i]
            if chX != chY:
                distance += 1
        return distance
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalDistance = 0
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                x = nums[i]
                y = nums[j]
                totalDistance += self.hammingDistance(x, y)
        return totalDistance

"""
Other solutions
https://discuss.leetcode.com/topic/72095/python-explanation
"""
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [[0, 0] for _ in xrange(32)]
        for num in nums:
            stringNum = format(num, 'b').zfill(32)
            for i in xrange(32):
                if stringNum[i] == '0':
                    bits[i][0] += 1
                else:
                    bits[i][1] += 1
        return sum(x*y for x, y in bits)
