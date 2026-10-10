class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        minute=0
        fresh=0
        queue=deque([])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2:
                    queue.append([row,col])
                elif grid[row][col]==1:
                    fresh+=1
        if fresh==0:
            return 0
        

        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        while queue:
            rotted=False
            for i in range(len(queue)):
                curr_r, curr_c=queue.popleft()
                for dr,dc in directions:
                    nr,nc=curr_r+dr,curr_c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        queue.append([nr,nc])
                        rotted=True
            if rotted:
                minute+=1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    return -1
        return minute