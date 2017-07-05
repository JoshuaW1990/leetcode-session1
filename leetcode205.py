class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sourceMap, targetMap = dict(), dict()
        for i in xrange(len(s)):
            source = sourceMap.get(t[i], None)
            target = targetMap.get(s[i], None)
            if source is None and target is None:
                sourceMap[t[i]] = s[i]
                targetMap[s[i]] = t[i]
            elif source != s[i] or target != t[i]:
                return False
        return True
