class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n
        while num > 1:
            if num % 2 != 0:
                return False
            else:
                num /= 2
        if num == 1:
            return True
        else:
            return False
