class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        H={}
        n=len(hand)
        if n%groupSize:
            return False
        for h in hand:
	        H[h]=1+H.get(h,0)
        heap=list(H.keys())
        heapq.heapify(heap)

        while heap:
            first=heap[0]
            for i in range(first, first+groupSize):
                if i not in H:
                    return False
                H[i]-=1
                if H[i]==0:
                    heapq.heappop(heap)
        return True
                
