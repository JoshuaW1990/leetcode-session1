class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        def helper(num, h=''):
            return (not num or h[7:]) and h or helper(num / 16, '0123456789abcdef'[num % 16] + h)
        return helper(num)
