class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row in range(0, 9):
            myset = set()
            for j in range(0, 9):
                if board[row][j] != '.' and board[row][j] in myset:
                    return False
                myset.add(board[row][j])
        
        # columns
        for i in range(0, 9):
            myset = set()
            for row in range(0, 9):
                if board[row][i] != '.' and board[row][i] in myset:
                    return False
                myset.add(board[row][i])
        
        # each 3x3 box
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                myset = set()
                for i in range(row, row+3):
                    for j in range(col, col+3):
                        if board[i][j] != '.' and board[i][j] in myset:
                            return False
                        myset.add(board[i][j])
        
        return True