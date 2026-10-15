class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=len(height)-1
        maxl=height[0]
        maxr=height[n-1]
        res=0
        while l<r:
            if maxl<maxr:
                l+=1
                maxl=max(maxl,height[l])
                res+=maxl-height[l]
            else:
                r-=1
                maxr=max(maxr,height[r])
                res+=maxr-height[r]
        return res

            



        