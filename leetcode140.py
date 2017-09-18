class Solution(object):
    def dpSolver(self, s, wordDict):
        dp = [False for _ in xrange(len(s) + 1)]
        dp[0] = True
        for i in xrange(1, len(s) + 1):
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        def dfs(validSentence, index):
            if index == len(s):
                res.append(" ".join(validSentence))
            for i in xrange(index + 1, len(s) + 1):
                if dp[i] is False:
                    continue
                if s[index: i] in wordDict:
                    dfs(validSentence + [s[index: i]], i)

        dp = self.dpSolver(s, wordDict)
        if dp[-1] is False:
            return []
        res = []
        dfs([], 0)
        return res
