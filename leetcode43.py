class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0 for _ in xrange(len(num1) + len(num2))] 
        for i, digit1 in enumerate(reversed(num1)):
            for j, digit2 in enumerate(reversed(num2)):
                res[i + j] += int(digit1) * int(digit2)
                res[i + j + 1] += res[i + j] / 10
                res[i + j] %= 10
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return ''.join(map(str, reversed(res)))

