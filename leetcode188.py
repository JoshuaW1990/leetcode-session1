class Solution(object):
    def maxProfit(self, k, prices):
        """

		global[i][j]=max(local[i][j],global[i-1][j])，

		local[i][j]=max(global[i-1][j-1]+max(diff,0),local[i-1][j]+diff)

        :type k: int
        :type prices: List[int]
        :rtype: int
        """
		length = len(prices)
        if length == 0:
            return 0
		# k is big enougth to cover all ramps.
        if k >= length / 2:
            return sum(i - j
                       for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        local_profit = [0] * (k+1)
        global_profit = [0] * (k+1)
        for i in xrange(length - 1):
            diff = prices[i + 1] - prices[i]
            for j in xrange(k, 0, -1):
                local_profit[j] = max(global_profit[j - 1] + max(diff, 0), local_profit[j] + diff)
                global_profit[j] = max(local_profit[j], global_profit[j])
        return global_profit[k]