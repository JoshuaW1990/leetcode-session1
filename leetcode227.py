class Solution(object):
    def helper(self, stack, sign, number):
        if sign == '+':
            stack.append(number)
        elif sign == '-':
            stack.append(-number)
        elif sign == '*':
            stack.append(stack.pop() * number)
        else:
            # The integer division should truncate toward zero.
            tmp = stack.pop()
            if tmp // number < 0 and tmp % number != 0:
                stack.append(tmp // number + 1)
            else:
                stack.append(tmp // number)
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        stack = []
        sign = '+'
        while i <= len(s):
            if i == len(s):
                self.helper(stack, sign, number)
                break
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                number = int(s[start:i])
                continue
            if c in '+-*/':
                self.helper(stack, sign, number)
                sign = c
            i += 1
        return sum(stack)
