class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph={i:[] for i in range(n)}

        for source, dest, price in flights:
            graph[source].append((dest,price))
        
        heap=[(0,0,src)]#middle index represents countert to track number of stops.
        visited={}
        while heap:
            curr_price, stops, airport=heapq.heappop(heap)
            if stops>k+1:
                continue
            if airport==dst:
                return curr_price
            if airport in visited and visited[airport]<stops:#minstops[airport]<stops is enough since the heap anyway handles cheaper paths earlier 
                continue
            visited[airport]=stops
            for nxt, add_price in graph[airport]:
                heapq.heappush(heap, (add_price+curr_price, stops+1, nxt ))
        return -1
    

        