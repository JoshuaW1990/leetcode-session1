"""
first session
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        n = len(prices)
        for i in range(n - 1):
            if prices[i] < prices[i + 1]:
                result += prices[i + 1] - prices[i]
        return result

"""
second session
"""
# Greedy Algorithm
class Solution(object):
    def maxProfit(self, prices):
        """
        Use greedy algorithm
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        length = len(prices)
        for i in xrange(length - 1):
            if prices[i] <= prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit
        