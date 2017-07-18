class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        n = len(candies) / 2
        candySet = set(candies)
        return min(n, len(candySet))
