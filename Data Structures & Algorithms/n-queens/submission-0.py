class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        grid=[['.']*n for i in range(n)]

        danger_cols=set()
        #danger_rows=set()
        danger_pos_diag=set()
        danger_neg_diag=set()
        res=[]
        def dfs(row_idx):
            if row_idx==n:
                res.append(["".join(row) for row in grid])
                return 

            for c in range(n):
                new_row_idx=row_idx+1
                if c not in danger_cols and c+row_idx not in danger_pos_diag and row_idx-c not in danger_neg_diag:
                    grid[row_idx][c]='Q'
                    danger_cols.add(c)
                    danger_pos_diag.add(c+row_idx)
                    danger_neg_diag.add(row_idx-c)
                    
                    dfs(new_row_idx)
                    danger_cols.remove(c)
                    danger_pos_diag.remove(c+row_idx)
                    danger_neg_diag.remove(row_idx-c)
                    grid[row_idx][c]='.'
                
            return
        dfs(0)
        return res

