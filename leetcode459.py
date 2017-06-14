class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        for i in xrange(1, length / 2 + 1):
            if length % i != 0:
                continue
            else:
                substring = s[:i]
                if substring * (length / i) == s:
                    return True
        return False
