class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m=max(piles)
        n=len(piles)
        l=1
        r=m
        mink=m
        
        while(l<=r):
            mid=(l+r)//2
            res=0
            for i in range(n):
                res=res+math.ceil(piles[i]/mid)
            if res<=h:
                mink=min(mink,mid)
                r=mid-1
            else:
                l=mid+1
        return mink



        