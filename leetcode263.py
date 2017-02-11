class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        tmp = num
        while tmp % 2 == 0:
            tmp = tmp / 2
        while tmp % 3 == 0:
            tmp = tmp / 3
        while tmp % 5 == 0:
            tmp = tmp / 5
        if tmp == 1:
            return True
        else:
            return False
        
