class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path=[]
        rows=len(board)
        cols=len(board[0])

        def dfs(index,r,c):
            if index==len(word):
                return True
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[index]:
                return False
            
            directions=[(1,0),(0,1),(-1,0),(0,-1)]
            tmp=board[r][c]
            board[r][c]='#'
            for dr, dc in directions:
                nr, nc= r+dr, c+dc
                if dfs(index+1,nr,nc):
                    return True
            board[r][c]=tmp

        for row in range(rows):
            for col in range(cols):
                if dfs(0,row,col):
                    return True
        return False

            