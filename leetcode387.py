class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dupSet = set()
        firstSet = set()
        for ch in s:
            if ch in dupSet:
                continue
            if ch in firstSet:
                firstSet.remove(ch)
                dupSet.add(ch)
            else:
                firstSet.add(ch)
        for i, ch in enumerate(s):
            if ch in firstSet:
                return i
        return -1
