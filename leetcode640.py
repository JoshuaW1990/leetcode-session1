class Solution(object):
    def helper(self, eq):
        start = 0
        index = 0
        const = 0
        coef = 0
        while index < len(eq):
            ch = eq[index]
            if '0' <= ch <= '9':
                start = index
                while index < len(eq) and '0' <= eq[index] <= '9':
                    index += 1
                num = int(eq[start:index])
                if eq[start-1] == '-':
                    num = -num
                if index == len(eq) or eq[index] != 'x':
                    const += num
                else:
                    coef += num
            elif ch == 'x':
                if index == 0:
                    coef += 1
                else:
                    if eq[index-1] == '-':
                        coef -= 1
                    else:
                        coef += 1
            index += 1
        return const, coef

    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        constLeft, coefLeft = self.helper(left)
        constRight, coefRight = self.helper(right)
        coef = coefLeft - coefRight
        const = constRight - constLeft
        if coef == 0:
            if const == 0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            return 'x='+str(const / coef)
