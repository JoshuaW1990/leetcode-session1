class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        result = strs[0]
        for item in strs[1:]:
            for i in xrange(len(result)):
                if i == len(item) or result[i] != item[i]:
                    result = result[:i]
                    break
        return result
