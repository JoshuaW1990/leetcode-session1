class Solution(object):
    def hIndex(self, citations):
        """
        reference: https://discuss.leetcode.com/topic/38299/short-python-o-log-n-solution
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        begin, end = 0, length - 1
        while begin <= end:
            mid = (begin + end) / 2
            if citations[mid] >= length - mid:
                end = mid - 1
            else:
                begin = mid + 1
        return length - begin
