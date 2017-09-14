class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix[0]:
            return
        height = len(matrix)
        width = len(matrix[0])

        col_zero, row_zero = False, False
        for col in xrange(width):
            if matrix[0][col] == 0:
                row_zero = True
        for row in xrange(height):
            if matrix[row][0] == 0:
                col_zero = True

        for row in xrange(1, height):
            for col in xrange(1, width):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for col in xrange(1, width):
            if matrix[0][col] == 0:
                for row in xrange(1, height):
                    matrix[row][col] = 0
        for row in xrange(1, height):
            if matrix[row][0] == 0:
                for col in xrange(1, width):
                    matrix[row][col] = 0

        if row_zero:
            for col in xrange(width):
                matrix[0][col] = 0
        if col_zero:
            for row in xrange(height):
                matrix[row][0] = 0
