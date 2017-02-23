class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(n, start, k, result, item):
            for i in xrange(start, n - k + 2):
                if k == 1:
                    result.append(item + [i])
                else:
                    helper(n, i + 1, k - 1, result, item + [i])
            return result
        
        return helper(n, 1, k, [], [])
            
