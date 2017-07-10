class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        neighborCount = collections.defaultdict(int)
        high = len(grid)
        width = len(grid[0])
        neighbor = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for row in range(high):
            for col in xrange(width):
                if grid[row][col] == 0:
                    continue
                count = 0
                for x, y in neighbor:
                    newRow = row + x
                    newCol = col + y
                    if newRow < 0 or newRow >= high:
                        continue
                    if newCol < 0 or newCol >= width:
                        continue
                    if grid[newRow][newCol] == 1:
                        count += 1
                neighborCount[count] += 1
        ans = 0
        for i in xrange(5):
            ans += (4 - i) * neighborCount[i]
        return ans


"""
No dict
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        high = len(grid)
        width = len(grid[0])
        neighbor = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ans = 0
        for row in range(high):
            for col in xrange(width):
                if grid[row][col] == 0:
                    continue
                count = 0
                for x, y in neighbor:
                    newRow = row + x
                    newCol = col + y
                    if newRow < 0 or newRow >= high:
                        continue
                    if newCol < 0 or newCol >= width:
                        continue
                    if grid[newRow][newCol] == 1:
                        count += 1
                ans += 4 - count
        return ans


"""
http://bookshadow.com/weblog/2016/11/20/leetcode-island-perimeter/
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0]) if h else 0
        ans = 0
        for x in range(h):
            for y in range(w):
                if grid[x][y] == 1:
                    ans += 4
                    if x > 0 and grid[x - 1][y]:
                        ans -= 2
                    if y > 0 and grid[x][y - 1]:
                        ans -= 2
        return ans
