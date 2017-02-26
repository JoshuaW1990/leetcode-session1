class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        # use the first element in each row to determine sublist quickly and search the sublist
        if matrix == [] or matrix == [[]]:
            return False
        # get the height and width
        height, width = len(matrix), len(matrix[0])
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        begin, end = 0, height - 1
        while begin < end - 1:
            mid = (begin + end) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                begin = mid
            else:
                end = mid
        if matrix[end][0] <= target:
            idx = end
        else:
            idx = begin
        begin, end = 0, width - 1
        while begin < end - 1:
            mid = (begin + end) / 2
            if matrix[idx][mid] == target:
                return True
            elif matrix[idx][mid] < target:
                begin = mid
            else:
                end = mid
        if matrix[idx][begin] == target or matrix[idx][end] == target:
            return True
        else:
            return False
