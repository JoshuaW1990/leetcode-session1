class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch_dict = dict()
        for ch in s:
            if ch not in ch_dict:
                ch_dict[ch] = 1
            else:
                ch_dict[ch] += 1
        result = 0
        for key in ch_dict.keys():
            if ch_dict[key] % 2 == 0:
                result += ch_dict[key]
                del ch_dict[key]
            else:
                result += ch_dict[key] - 1
                ch_dict[key] = 1
        if len(ch_dict) > 0:
            result += 1
        return result