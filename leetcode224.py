"""
https://discuss.leetcode.com/topic/15806/easy-18-lines-c-16-lines-python
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i, sign = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                result += sign.pop() * int(s[start:i])
                continue
            if c in '+-(':
                if c in '+(':
                    sign += [sign[-1]]
                else:
                    sign += [-sign[-1]]
            elif c == ')':
                sign.pop()
            i += 1
        return result


"""
http://bookshadow.com/weblog/2015/06/09/leetcode-basic-calculator/
"""
class Solution(object):
    priorityDict = {'+': 1, '-':1, '*':2, '/':2}

    def toRPN(self, s):
        i = 0
        rpnList, stack = [], []
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                rpnList.append(s[start:i])
                continue
            if c in self.priorityDict.keys():
                while stack and stack[-1] in self.priorityDict.keys() and self.priorityDict[stack[-1]] >= self.priorityDict[c]:
                    rpnList.append(stack.pop())
                stack.append(c)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while stack and stack[-1] != '(':
                    rpnList.append(stack.pop())
                stack.pop()
            i += 1
        while stack:
            rpnList.append(stack.pop())
        return rpnList

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        rpnList = self.toRPN(s)
        stack = []
        for item in rpnList:
            if item not in self.priorityDict.keys():
                stack.append(int(item))
            else:
                reg2 = stack.pop()
                reg1 = stack.pop()
                if item == '+':
                    stack.append(reg1 + reg2)
                elif item == '-':
                    stack.append(reg1 - reg2)
                elif item == '*':
                    stack.append(reg1 * reg2)
                else:
                    stack.append(reg1 / reg2)
        return stack[0]
