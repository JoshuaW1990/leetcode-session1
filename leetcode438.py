"""
https://discuss.leetcode.com/topic/64412/python-sliding-window-solution-using-counter
"""

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p) - 1])
        for i in xrange(len(p) - 1, len(s)):
            sCounter[s[i]] += 1
            if pCounter == sCounter:
                result.append(i - len(p) + 1)
            sCounter[s[i - len(p) + 1]] -= 1
            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]
        return result

