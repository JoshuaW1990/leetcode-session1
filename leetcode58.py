class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(string):
            ch_list = string.split('')
            result = 0
            for ch in ch_list:
                if 'a' <= ch <= 'z' and 'A' <= ch <= 'Z':
                    result += 1
            return result

        string_list = s.split(' ')
        for i in xrange(len(string_list), -1, -1):
            string = string_list[i]
            length = helper(string)
            if length > 0:
                return length
        return length