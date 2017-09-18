class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in xrange(len(p) + 1)] for j in xrange(len(s) + 1)]
        dp[0][0] = True
        for i in xrange(len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if i > 0 and (s[i-1] == p[j-1] or p[j-1] == '.'):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if dp[i][j-2]:
                        dp[i][j] = True
                    elif i > 0 and (s[i-1] == p[j-2] or p[j-2] == '.'):
                        dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = False
        print dp
        return dp[-1][-1]