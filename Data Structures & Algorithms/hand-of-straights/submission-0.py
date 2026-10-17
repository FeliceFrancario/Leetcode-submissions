class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        H={}
        n=len(hand)
        if n%groupSize:
            return False
        n_groups=n//groupSize
        for h in hand:
	        H[h]=1+H.get(h,0)
        
        for g in range(n_groups):
            curr=min(H)
            for i in range(groupSize):
	            if (curr+i) not in H:
		            return False
	            H[curr+i]-=1
	            if H[curr+i]==0:
		            del H[curr+i]
        return len(H)==0
