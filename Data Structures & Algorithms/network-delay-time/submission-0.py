class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        visited=set()
        t=0
        heap=[(0,k)]
        while heap:
            w, node= heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t=max(t,w)
            for neighbour,weight in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(heap,(weight+w,neighbour))

            
        return t if len(visited)==n else -1

            

        