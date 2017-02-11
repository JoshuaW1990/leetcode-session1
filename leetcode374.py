# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bisection method
        low = 0
        high = n
        
        def guessHighLow(low, high):
            if (high + low) % 2 == 1:
                mid = (high + low ) / 2 + 1
            else:
                mid = (high + low ) / 2
            if guess(mid) == 1:
                return guessHighLow(mid, high)
            elif guess(mid) == -1:
                return guessHighLow(low, mid)
            else:
                return mid
        
        return guessHighLow(low, high)
