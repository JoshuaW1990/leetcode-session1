"""
first session
"""
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

"""
second session
"""
# reference:
# http://blog.csdn.net/linhuanmars/article/details/23236995

class Solution(object):
    def maxProfit(self, prices):
        """

        global[i][j]=max(local[i][j],global[i-1][j])，

        local[i][j]=max(global[i-1][j-1]+max(diff,0),local[i-1][j]+diff)

        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        local_profit = [0] * 3
        global_profit = [0] * 3
        for i in xrange(length - 1):
            diff = prices[i + 1] - prices[i]
            for j in range(2, 0, -1):
                local_profit[j] = max(global_profit[j - 1] + max(diff, 0), local_profit[j] + diff)
                global_profit[j] = max(local_profit[j], global_profit[j])
        return global_profit[2]