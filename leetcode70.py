class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 1
        DP = [0 for _ in xrange(n + 1)]
        DP[0] = 1
        DP[1] = 1
        for i in xrange(2, n + 1):
            DP[i] = DP[i - 1] + DP[i - 2]
        return DP[-1]