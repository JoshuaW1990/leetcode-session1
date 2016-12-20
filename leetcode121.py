"""
Previous Solution
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minp = float('inf')
        prof = 0
        for i in prices:
            print minp
            if i <= minp:
                minp = i
                continue
            if i > minp:
                prof = max( prof, i - minp )
        return prof

"""
Solution with DP
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        DP = [0 for i in xrange(length)]
        if length <= 1:
            return 0
        DP[0] = 0
        minValue = prices[0]
        for i in xrange(1, length):
            price = prices[i]
            DP[i] = max(price - minValue, DP[i - 1])
            if minValue > price:
                minValue = price
        return DP[-1]