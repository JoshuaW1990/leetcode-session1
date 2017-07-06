class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        tmp = n
        while tmp > 0:
            rem = (tmp - 1) % 26
            ch = chr(ord('A') + rem)
            ans = ch + ans
            tmp = (tmp - 1) / 26
        return ans
