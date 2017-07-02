class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        myDict = {}
        myDict[2] = ['a', 'b', 'c']
        for i in xrange(3, 7):
            myDict[i] = []
            for ch in myDict[i - 1]:
                myDict[i].append(chr(ord(ch) + 3))
        myDict[7] = list('pqrs')
        myDict[8] = list('tuv')
        myDict[9] = ['w', 'x', 'y', 'z']
        result = []

        def helper(current, digits):
            if digits == '':
                if current != '':
                    result.append(current)
                return
            digit = int(digits[0])
            for ch in myDict[digit]:
                helper(current + ch, digits[1:])

        helper('', digits)
        return result
