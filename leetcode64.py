class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid[0]:
            return 0
        height = len(grid)
        width = len(grid[0])
        dp = [0 for _ in xrange(width)]
        # initialization
        dp[0] = grid[0][0]
        for i in xrange(1, width):
            dp[i] = dp[i - 1] + grid[0][i]
        for i in xrange(1, height):
            dp[0] = dp[0] + grid[i][0]
            for j in xrange(1, width):
                dp[j] = grid[i][j] + min(dp[j - 1], dp[j])
        return dp[-1]
