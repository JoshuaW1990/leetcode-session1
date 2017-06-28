class Solution(object):
    def dfs(self, board, location, visited, ch_list):
        if len(ch_list) == 0:
            return True
        x, y = location
        tmpSet = {(x, y)}
        # up
        if x - 1 >= 0 and (x - 1, y) not in visited and board[x - 1][y] == ch_list[0]:
            if self.dfs(board, (x - 1, y), visited | tmpSet, ch_list[1:]):
                return True
        # down
        if x + 1 < len(board) and (x + 1, y) not in visited and board[x + 1][y] == ch_list[0]:
            if self.dfs(board, (x + 1, y), visited | tmpSet, ch_list[1:]):
                return True
        # left
        if y - 1 >= 0 and (x, y - 1) not in visited and board[x][y - 1] == ch_list[0]:
            if self.dfs(board, (x, y - 1), visited | tmpSet, ch_list[1:]):
                return True
        # right
        if y + 1 < len(board[0]) and (x, y + 1) not in visited and board[x][y + 1] == ch_list[0]:
            if self.dfs(board, (x, y + 1), visited | tmpSet, ch_list[1:]):
                return True

        return False



    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    word_list = list(word)
                    visited = set()
                    location = (i, j)
                    if self.dfs(board, location, visited, word_list[1:]):
                        return True
        return False
