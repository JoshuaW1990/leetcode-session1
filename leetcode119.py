class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        current_row = [1]
        for i in xrange(rowIndex + 1):
            prev_row = current_row
            current_row = [0 for _ in xrange(i + 1)]
            current_row[0] = 1
            current_row[-1] = 1
            for j in xrange(1, i):
                current_row[j] = prev_row[j - 1] + prev_row[j]
        return current_row