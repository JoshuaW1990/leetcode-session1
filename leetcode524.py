class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        d.sort(key=lambda x: (-len(x), x))
        return next(itertools.ifilter(isSubsequence, d), '')

