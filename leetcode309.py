class Solution(object):
    def maxProfit(self, prices):
        """

		delta = prices[i] - prices[i - 1]
		sells[i] = max(buys[i - 1] + prices[i], sells[i - 1] + delta) 
		buys[i] = max(sells[i - 2] - prices[i], buys[i - 1] - delta)

        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
		if length < 2:
			return 0
		sells = [0] * length
		buys = [0] * length
		buys[0] = -prices[0]
		for i in xrange(1, length):
			delta = prices[i] - prices[i - 1]
			sells[i] = max(buys[i-1]+prices[i], sells[i-1]+delta)
			if i > 1:
				buys[i] = max(sells[i-2]-prices[i], buys[i-1]-delta)
			else:
				buys[i] = buys[i-1] - delta
		return max(sells)