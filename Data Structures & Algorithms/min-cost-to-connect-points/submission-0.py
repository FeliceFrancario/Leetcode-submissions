class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        graph={i:[] for i in range(N)}

        for i in range(N):
            x1, y1= points[i]
            for j in range(i,N):
                x2,y2=points[j]
                dist=abs(x2-x1)+abs(y2-y1)
                graph[i].append([dist,j])
                graph[j].append([dist,i])

        res=0
        heap=[(0,0)]
        visited=set()

        while len(visited)<N:
            dist, point=heapq.heappop(heap)
            if point in visited:
                continue
            res+=dist
            visited.add(point)
            for cost, neigh in graph[point]:
                if neigh not in visited:
                    heapq.heappush(heap,[cost,neigh])
        return res

            


