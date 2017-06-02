"""
Naive solution
looping in the whole array and find the maximum value for each one

It is very inefficient
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [] 
        length = len(nums)
        if length == 0:
            return []
        for startIndex in xrange(length - k + 1):
            endIndex = startIndex + k
            subsequence = nums[startIndex:endIndex]
            result.append(max(subsequence))
        return result 


"""
Advanced algorithm
http://bookshadow.com/weblog/2015/07/18/leetcode-sliding-window-maximum/
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = collections.deque()
        ans = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if dq[0] == i - k:
                dq.popleft()
            if i >= k - 1:
                ans.append(nums[dq[0]])
        return ans
