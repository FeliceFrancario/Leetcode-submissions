class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []
        rows=len(heights)
        cols=len(heights[0])
        pacific=set()
        atlantic=set()
        
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        
        def dfs(r,c,ocean):
            if (r,c) in ocean:
                return 
            ocean.add((r,c))
            for dr,dc in directions:
                nr, nc =r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,ocean)
        
        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row,cols-1,atlantic)
        for col in range(cols):
            dfs(0,col, pacific)
            dfs(rows-1,col,atlantic)
        return list(pacific.intersection(atlantic))


        