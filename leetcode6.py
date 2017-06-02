"""
Niave solution
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        matrix = []
        i = 0
        while i < len(s):
            current_column = ['' for _ in xrange(numRows)]
            for j in xrange(numRows):
                rem = len(matrix) % (numRows - 1)
                if rem == 0 or rem == (numRows - j - 1):
                    if i >= len(s):
                        current_column[j] = ''
                    else:
                        current_column[j] = s[i]
                else:
                    continue
                i += 1
            matrix.append(current_column)
        result = []
        for i in xrange(numRows):
            for j in xrange(len(matrix)):
                result.append(matrix[j][i])
        return ''.join(result)

"""
Advanced solution
https://discuss.leetcode.com/topic/34573/python-o-n-solution-in-96ms-99-43/3
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        step = (numRows == 1) - 1  # 0 or -1  
        rows, idx = [''] * numRows, 0
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows-1: 
                step = -step  #change direction  
            idx += step
        return ''.join(rows)



