class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            heapq.heappush(heap,(-math.sqrt(point[0]*point[0]+point[1]*point[1]), point))
            if len(heap)>k:
                heapq.heappop(heap)
        return [h[1] for h in heap]
