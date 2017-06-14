class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        reversed_num1 = list(reversed(num1))
        reversed_num2 = list(reversed(num2))
        length = max(len(num1), len(num2))
        res = [0 for _ in xrange(length + 1)]
        for i in xrange(length):
            if i < len(reversed_num1):
                digit1 = reversed_num1[i]
            else:
                digit1 = '0'
            if i < len(reversed_num2):
                digit2 = reversed_num2[i]
            else:
                digit2 = '0'
            res[i] += int(digit1) + int(digit2)
            res[i + 1] += res[i] / 10
            res[i] %= 10
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return ''.join(map(str, reversed(res)))