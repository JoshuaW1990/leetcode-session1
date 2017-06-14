"""
Naive solution:
1. Run LCS for the strings
2. compare the LCS result with the length of the strings
"""

class Solution(object):
    def LCS(self, string1, string2):
        DP = [[0 for i in xrange(len(string2) + 1)] for j in xrange(len(string1) + 1)]
        for i in xrange(1, len(string1) + 1):
            for j in xrange(1, len(string2) + 1):
                if string1[i - 1] == string2[j - 1]:
                    DP[i][j] = DP[i - 1][j - 1] + 1
                else:
                    DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
        return DP[-1][-1]




    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        length_LCS = self.LCS(word1, word2)
        result = len(word1) - length_LCS
        result += len(word2) - length_LCS
        return result