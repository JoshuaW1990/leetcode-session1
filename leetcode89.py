class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # https://discuss.leetcode.com/topic/4883/one-liner-python-solution-with-demo-in-comments/2
        result = [0]
        for i in xrange(n):
            result += [x + 2**i for x in reversed(result)]
        return result
