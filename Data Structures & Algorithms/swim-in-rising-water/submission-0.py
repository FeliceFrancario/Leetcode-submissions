class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap=[[grid[0][0],(0,0)]]
        rows=len(grid)
        cols=len(grid[0])
        #queue=deque([(0,0)])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        visited=set()
        time=0
        while heap:
            curr_val, (curr_r,curr_c)=heapq.heappop(heap)
            if (curr_r,curr_c) in visited:
                continue
            time=max(time,curr_val)
            if (curr_r,curr_c)==(rows-1,cols-1):
                return time
            visited.add((curr_r,curr_c))
            for dr, dc in directions:
                nr, nc=curr_r+dr, curr_c+dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited:
                    heapq.heappush(heap,[grid[nr][nc],(nr,nc)])
            



