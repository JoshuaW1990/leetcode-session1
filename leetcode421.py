class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = mask = 0
        for i in xrange(31, -1, -1):
            mask = mask | (1 << i)
            prefixSet = set([num & mask for num in nums])
            tmp = result | (1 << i)
            for item in prefixSet:
                if item ^ tmp in prefixSet:
                    result = tmp
                    break
        return result
