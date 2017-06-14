class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        DP = [[0 for i in xrange(len(word2) + 1)] for j in xrange(len(word1) + 1)]
        # initialization
        for i in xrange(len(word1) + 1):
            DP[i][0] = i
        for i in xrange(len(word2) + 1):
            DP[0][i] = i
        # DP algorithm
        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                DP[i][j] = min(DP[i - 1][j] + 1, DP[i][j - 1] + 1, DP[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1))
        return DP[-1][-1]