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


"""
Second sessions
"""
# Naive solution
class Solution(object):
    def maxProfit(self, prices):
        """
        Naive solution:
        Find all transaction combination and compare them one by one
        Problem: Will cause time limited exceeded when test case is very large
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)    
        maxProfit = 0
        for i in xrange(length):
            for j in xrange(i + 1, length):
                profit = prices[j] - prices[i]
                maxProfit = max(profit, maxProfit)
        return maxProfit

# DP algorithm
class Solution(object):
    def maxProfit(self, prices):
        """
        DP algorithm:
        DP table: [(maxProfit, minArray), ...,]

        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        DP = [(0, 0)] * length
        DP[0] = (0, prices[0])
        for i in xrange(1, length):
            profit = prices[i] - DP[i - 1][1]
            maxProfit = max(profit, DP[i - 1][0])
            minArray = min(prices[i], DP[i - 1][1])
            DP[i] = (maxProfit, minArray)
        return DP[-1][0]