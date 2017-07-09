class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sumArray = [0]
        for num in nums:
            self.sumArray.append(self.sumArray[-1] + num)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumArray[j + 1] - self.sumArray[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
