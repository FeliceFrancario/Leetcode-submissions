class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows=len(board)
        cols=len(board[0])
        H_row=set()
        H_col=set()
        H_square=set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='.':
                    continue
                if board[r][c] in H_row:
                    return False
                else:
                    H_row.add(board[r][c])
            H_row=set()

        for c in range(rows):
            for r in range(cols):
                if board[r][c]=='.':
                    continue
                if board[r][c] in H_col:
                    return False
                else:
                    H_col.add(board[r][c])
            H_col=set()
        
        for square in range(9):
            for i in range(3):
                for j in range(3):
                    row=(square//3)*3+i
                    col=(square%3)*3+j
                    if board[row][col]=='.':
                        continue
                    if board[row][col] in H_square:
                        return False
                    H_square.add(board[row][col])
            H_square=set()
        return True
                    