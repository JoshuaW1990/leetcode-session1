class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        x = 5
        while n >= x:
            result += n / x
            x *= 5
        return result
