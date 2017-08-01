class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = set()
        start = end = 0
        maxLength = 0
        while end < len(s):
            if s[end] not in visited:
                visited.add(s[end])
                maxLength = max(maxLength, len(visited))
            else:
                while s[start] != s[end] and start < end:
                    visited.remove(s[start])
                    start += 1
                start += 1
                maxLength = max(maxLength, len(visited))
            end += 1
        return maxLength