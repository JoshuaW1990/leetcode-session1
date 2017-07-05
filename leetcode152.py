class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        maxCurr = minCurr = maxTotal = nums[0]

        for num in nums[1:]:
            maxCurr, minCurr = max([num, minCurr * num, maxCurr * num]), min([num, minCurr * num, maxCurr * num])
            maxTotal = max(maxTotal, maxCurr)
            print maxCurr, minCurr, maxTotal

        return maxTotal




"""
http://bookshadow.com/weblog/2014/10/15/leetcode-maximum-product-subarray/
"""
class Solution(object):
    def maxProduct(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = max(A)
        size = len(A)
        positive_max = [0 for x in range(size)]
        negative_min = [0 for x in range(size)]
        if A[0] > 0:
            positive_max[0] = A[0]
        elif A[0] < 0:
            negative_min[0] = A[0]
        for x in range(1, size):
            if A[x] > 0:
                positive_max[x] = max(positive_max[x - 1] * A[x], A[x])
                negative_min[x] = negative_min[x - 1] * A[x]
            elif A[x] < 0:
                positive_max[x] = negative_min[x - 1] * A[x]
                negative_min[x] = min(positive_max[x - 1] * A[x], A[x])
            if positive_max[x] and positive_max[x] > ans:
                ans = positive_max[x]
        return ans
