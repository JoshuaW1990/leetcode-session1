class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        """
        To define the validator of the sudoku:
        check the row, column and the submatrix
        """
        # naive solution: check row, column, and matrix one by one
        # row
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in visited or board[i][j] > '9' or board[i][j] < '0':
                    return False
                else:
                    visited.add(board[i][j])
        # column
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] in visited or board[j][i] > '9' or board[j][i] < '0':
                    return False
                else:
                    visited.add(board[j][i])
        # submatrix
        for i in range(3):
            for j in range(3):
                visited = set()
                for m in range(3):
                    for n in range(3):
                        row_idx = 3 * i + m
                        col_idx = 3 * j + n
                        if board[row_idx][col_idx] == '.':
                            continue
                        elif board[row_idx][col_idx] in visited or board[row_idx][col_idx] > '9' or board[row_idx][col_idx] < '0':
                            return False
                        else:
                            visited.add(board[row_idx][col_idx])
        return True
