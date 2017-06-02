class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length = len(s)
        if length <= 2 * k:
        	return s[k-1::-1] + s[k:]
        return s[k-1::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k)