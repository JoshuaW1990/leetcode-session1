class Solution(object):
    def isValid(self, s):
        """
        Use stack
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                newCh = stack.pop()
                if (ch == ')' and newCh != '(') or (ch == ']' and newCh != '[') or (ch == '}' and newCh != '{'):
                    return False
        return len(stack) == 0
