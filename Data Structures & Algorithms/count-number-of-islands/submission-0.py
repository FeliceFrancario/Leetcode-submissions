class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        def dfs(x,y):
            if x<0 or x>=cols or y>=rows or y<0 or grid[y][x]=='0':
                return
            grid[y][x]='0'
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        for a in range(rows):
            for b in range(cols):
                if grid[a][b]=='1':
                    islands+=1
                    dfs(b,a)
        return islands

            