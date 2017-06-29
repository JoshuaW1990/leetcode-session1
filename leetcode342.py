class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and 4 ** round(math.log(num,4)) == num


"""
Use the binary number
"""
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        binaryNum = bin(num)
        binaryList = list(binaryNum)
        binaryList.reverse()
        index = binaryList.index('1')
        return index % 2 == 0 and binaryNum.count('1') == 1
