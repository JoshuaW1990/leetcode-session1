class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use DP + stack
        l = len(s)
        if l == 0:
            return 0
        dp = [0 for _ in xrange(l)]
        stack = []
        for i in xrange(l):
            if s[i] == '(':
                stack.append(i)
            elif stack == []:
                continue
            else:
                x = stack.pop()
                if x > 0:
                    dp[i] = (i - x + 1) + dp[x - 1]
                else:
                    dp[i] = i - x + 1
        return max(dp)