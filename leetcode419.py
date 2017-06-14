class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def getNeighbor(e, visited, height, width):
            (x, y) = e
            result = []
            for (i, j) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if i < 0 or i > height - 1:
                    continue
                if j < 0 or j > width - 1:
                    continue
                if (i, j) in visited:
                    continue
                result.append((i, j))
            return result

        height = len(board)
        width = len(board[0])
        count = 0
        visited = set()
        for i in xrange(height):
            for j in xrange(width):
                if (i, j) in visited:
                    continue
                if board[i][j] == '.':
                    visited.add((i, j))
                else:
                    stack = [(i, j)]
                    while stack:
                        e = stack.pop()
                        neighbors = getNeighbor(e, visited, height, width)
                        for item in neighbors:
                            visited.add(item)
                            x, y = item
                            if board[x][y] == 'X':
                                stack.append(item)
                    count += 1

        return count


"""
https://discuss.leetcode.com/topic/64834/python-solution
"""
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board) == 0: return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    count += 1
        return count