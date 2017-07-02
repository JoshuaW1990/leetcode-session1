class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        myDict = {}
        num = 0
        while num ** 2 <= c:
            value = num**2
            myDict[value] = num
            rem = c - value
            if rem in myDict:
                return True
            num += 1
        return False
