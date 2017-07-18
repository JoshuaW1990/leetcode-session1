class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops == []:
            return m * n
        rList, cList = zip(*ops)
        minRow = min(rList)
        minColumn = min(cList)
        minRow = min(minRow, m)
        minColumn = min(minColumn, n)
        return minRow * minColumn
