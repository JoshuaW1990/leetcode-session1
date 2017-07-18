class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        height = len(nums)
        width = len(nums[0])
        if height * width != r * c:
            return nums
        ans = []
        row = []
        for i in xrange(height):
            for j in xrange(width):
                num = nums[i][j]
                row.append(num)
                if len(row) == c:
                    ans.append(row)
                    row = []
        return ans
