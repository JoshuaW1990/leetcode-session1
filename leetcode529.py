class Solution(object):
    def countNeighbor(self, board, coords):
        """
        Calculate the number of mines around the given coords
        Returns:
            number of mines
            list of coords of 'E'
        """
        mine_number = 0
        neighbor_list = []
        height = len(board)
        width = len(board[0])
        row, col = coords
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i < 0 or i >= height:
                    continue
                if j < 0 or j >= width:
                    continue
                if i == row and j == col:
                    continue
                if board[i][j] == 'M':
                    mine_number += 1
                elif board[i][j] == 'E':
                    neighbor_list.append([i, j])
        return mine_number, neighbor_list
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        mine_number, neighbor_list = self.countNeighbor(board, click)
        if mine_number > 0:
            board[row][col] = str(mine_number)
        else:
            board[row][col] = 'B'
            for coord in neighbor_list:
                board = self.updateBoard(board, coord)
        return board
