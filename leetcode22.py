class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in xrange(2**(2*n)):
            num = bin(i)[2:]
            num = num.replace("1", "(")
            num = num.replace("0", ")")
            if num.count('(') != n:
                continue
            valid = 0
            for ch in num:
                if valid < 0:
                    break
                if ch == '(':
                    valid += 1
                else:
                    valid -= 1
            if valid == 0:
                result.append(num)
        return result


"""
Use backtracking
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def helper(current, left, right):
            if right == n:
                result.append(current)
                return
            if left < n:
                helper(current + '(', left + 1, right)
            if right < left:
                helper(current + ')', left, right + 1)

        helper('', 0, 0)
        return result
