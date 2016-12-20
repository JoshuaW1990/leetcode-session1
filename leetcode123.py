class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 1:
            return 0
        DP_order = [0 for i in xrange(length)]
        DP_reverse = [0 for i in xrange(length)]
        minPrice = prices[0]
        for i in xrange(1, length):
            minPrice = min(prices[i], minPrice)
            DP_order[i] = max(prices[i] - minPrice, DP_order[i - 1])
        maxPrice = prices[-1]
        for i in xrange(length - 2, -1, -1):
            maxPrice = max(prices[i], maxPrice)
            DP_reverse[i] = max(maxPrice - prices[i], DP_reverse[i + 1])
        maxProfit = 0
        for i in xrange(length):
            if i == 0:
                maxProfit = DP_reverse[i]
            else:
                maxProfit = max(maxProfit, DP_order[i - 1] + DP_reverse[i])
        return maxProfit
            
        