class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for ch in num:
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        index = 0
        while index < len(stack) and stack[index] == '0':
            index += 1
        if k > 0:
            result = stack[index:-k]  
        else:
            result = stack[index:]
        if len(result) == 0:
            return '0'
        else:
            return ''.join(result)