class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ch_list = list(s)
        ch_list.reverse()
        return ''.join(ch_list)