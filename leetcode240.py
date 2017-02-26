class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # use the normal solution
        # check the first and the last item in each sublist. Then do the binary search
        def binarySearch(idx, matrix, target):
            width = len(matrix[0])
            begin, end = 0, width
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
        
        if matrix == [] or matrix == [[]]:
            return False
        height, width = len(matrix), len(matrix[0])
        idx = 0
        while idx < height:
            if matrix[idx][0] <= target <= matrix[idx][-1]:
                if binarySearch(idx, matrix, target):
                    return True
            idx += 1
        return False
        
        
            
