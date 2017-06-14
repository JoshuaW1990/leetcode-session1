class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def preprocess(nums, k):
            stack = []
            drop = len(nums) - k
            for ch in nums:
                while drop > 0 and stack and stack[-1] < ch:
                    stack.pop()
                    drop -= 1
                stack.append(ch)
            return stack[:k]
                
        def merge(num1, num2):
            return [max(num1, num2).pop(0) for _ in num1 + num2]

        result = []
        for i in xrange(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                result.append(merge(preprocess(nums1, i), preprocess(nums2, k - i)))
        return max(result)