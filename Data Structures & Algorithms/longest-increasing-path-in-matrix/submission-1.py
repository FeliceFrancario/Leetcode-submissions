class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        memo={}
        #longest=0
        def dfs(r,c):
            #nonlocal longest
            directions=[(1,0),(0,1),(-1,0),(0,-1)]
            
            if (r,c) in memo:
                return memo[(r,c)]
            longest=1
            for dr, dc in directions:
                nr, nc=dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc]>matrix[r][c]:
                    longest=max(longest,1+ dfs(nr,nc))
            memo[(r,c)]=longest
            return memo[(r,c)]

        res=0
        for r in range(rows):
            for c in range(cols):
                res=max(res,dfs(r,c))

        return res




        