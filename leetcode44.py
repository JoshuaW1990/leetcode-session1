class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in xrange(len(p) + 1)] for j in xrange(len(s) + 1)]
        # initialization
        dp[0][0] = True
        for col in xrange(1, len(p) + 1):
            if p[col - 1] == '*':
                dp[0][col] = dp[0][col - 1]
        # updating the dp table
        for row in xrange(1, len(s) + 1):
            for col in xrange(1, len(p) + 1):
                i, j = row - 1, col - 1
                if s[i] == p[j] or p[j] == '?':
                    dp[row][col] = dp[row - 1][col - 1]
                elif p[j] != '*' and s[i] != p[j]:
                    dp[row][col] = False
                else:
                    dp[row][col] = dp[row][col - 1] | dp[row - 1][col - 1] | dp[row - 1][col]
        return dp[-1][-1]