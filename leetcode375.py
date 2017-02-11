class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dynamic programming
        dp_table = [[0] * (n + 1) for _ in range(n + 1)]
        for lo in xrange(n, 0, -1):
            for hi in xrange(lo + 1, n + 1):
                dp_table[lo][hi] = min(i + max(dp_table[lo][i - 1], dp_table[i + 1][hi]) for i in xrange(lo, hi))
        return dp_table[1][n]
