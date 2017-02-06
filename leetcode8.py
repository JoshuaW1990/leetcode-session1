class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        result = 0
        string = list(str)
        index = 0
        while string[index] == ' ':
            index += 1
        if string[index] == '+':
            flag = 1
            index += 1
        elif string[index] == '-':
            flag = -1
            index += 1
        else:
            flag = 1
        for i in xrange(index, len(string)):
            if string[i] < '0' or string[i] > '9':
                return result * flag
            num = int(string[i])
            result = result * 10 + num
            if result * flag > 2147483647:
                return 2147483647
            if result * flag < -2147483648:
                return -2147483648
        return result * flag
