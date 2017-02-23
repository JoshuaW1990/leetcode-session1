class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid == []:
            return 0
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        dp = [[0] * (width + 1) for _ in range(height + 1)]
        for i in range(height - 1, -1, -1):
            for j in range(width - 1, -1, -1):
                if i == height - 1 and j == width - 1:
                    dp[i][j] = 1 - obstacleGrid[i][j]
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
        return dp[0][0]
        
