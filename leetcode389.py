class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0
        for i, ch in enumerate(s):
            result += ord(t[i])
            result -= ord(ch)
        result += ord(t[-1])
        return chr(result)
