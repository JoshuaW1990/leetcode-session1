class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        queue = []
        absX = abs(x)
        while absX:
            queue.append(absX % 10)
            absX /= 10
        ans = 0
        while queue:
            ans = ans * 10 + queue.pop(0)
        if ans >= 2**31:
            return 0
        return (x / abs(x)) * ans


"""
Use String
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        neg = x / abs(x)
        strX = list(str(abs(x)))
        result = int(''.join(reversed(strX)))
        if result >= 2**31:
            return 0
        return neg * result
