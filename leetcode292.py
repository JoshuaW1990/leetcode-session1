class Solution(object):
    def canWinNim(self, n):
        """
        DP problem
        :type n: int
        :rtype: bool
        """
        if n <= 3:
            return True
        DP = [None for _ in xrange(4)]
        DP[:3] = [True, True, True]
        for i in xrange(3, n):
            DP[3] = (not DP[2]) or (not DP[1]) or (not DP[0])
            DP[:3] = DP[1:]
        return DP[3]


"""
http://bookshadow.com/weblog/2015/10/12/leetcode-nim-game/
"""
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 > 0
