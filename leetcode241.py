class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        def helper1(numbers, signs):
            if len(numbers) == 1:
                return [numbers[0]]
            else:
                result = []
                for i in xrange(1, len(numbers)):
                    number1 = helper1(numbers[:i], signs[:i - 1])
                    sign = signs[i - 1]
                    number2 = helper1(numbers[i:], signs[i:])
                    result += helper2(number1, number2, sign)
                return result
                
        def helper2(numberList1, numberList2, sign):
            result = []
            for number1 in numberList1:
                for number2 in numberList2:
                    if sign == '+':
                        result.append(number1 + number2)
                    elif sign == '-':
                        result.append(number1 - number2)
                    else:
                        result.append(number1 * number2)
            return result

        numberList = []
        signList = []
        number = ''
        for ch in input:
            if ch == '+' or ch == '-' or ch == '*':
                signList.append(ch)
                numberList.append(int(number))
                number = ''
            else:
                number += ch
        numberList.append(int(number))
        result = helper1(numberList, signList)
        return result
