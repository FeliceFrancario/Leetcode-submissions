class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        max_area=0
        rows=len(grid)
        cols=len(grid[0])

        def dfs(r,c):
            nonlocal curr_sum
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0:
                return
            curr_sum+=1
            grid[r][c]=0
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
            return 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    curr_sum=0
                    dfs(r,c)
                    max_area=max(max_area,curr_sum)
        return max_area
            

        