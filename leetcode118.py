class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        for i in xrange(1, numRows):
            width = i + 1
            row = [0 for _ in xrange(width)]
            row[0] = 1
            row[-1] = 1
            prev_row = result[-1]
            for j in xrange(1, i):
                row[j] = prev_row[j - 1] + prev_row[j]
            result.append(row)
        return result