class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in xrange(2, len(s) + 1):
            num = s[i - 2:i]
            if '10' <= num <= '26' and s[i - 1] != '0':
                dp.append(dp[i - 2] + dp[i - 1])
            elif num == '10' or num == '20':
                dp.append(dp[i - 2])
            elif s[i - 1] != '0':
                dp.append(dp[i - 1])
            else:
                return 0
        return dp[-1]

