class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        
        DP = [0 for i in xrange(len(s))]
        if s[0] in wordDict:
            DP[0] = 1
        else:
            DP[0] = -1
        
        for i in xrange(1, len(s)):
            index = i + 1
            word = s[:index]
            if word in wordDict:
                DP[i] = 1
            else:
                for j in xrange(len(word) - 1):
                    if DP[j] == -1:
                        continue
                    else:
                        if word[j + 1:] in wordDict:
                            DP[i] = 1
                            break
                if DP[i] == 0:
                    DP[i] = -1

        if DP[-1] == -1:
            return False
        else:
            return True
