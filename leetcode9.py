class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        y = 0
        tmp = x
        while tmp > 0:
            y = y * 10 + tmp % 10
            tmp /= 10
        return x == y
