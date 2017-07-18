class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        absValue = abs(num)
        sig = num / absValue
        ans = ''
        while absValue:
            ans = str(absValue % 7) + ans
            absValue /= 7
        if sig < 0:
            return '-' + ans
        else:
            return ans
