class Solution:
    def trap(self, height: List[int]) -> int:
       
        n=len(height)
        maxl=[0]*n
        maxr=[0]*n
        curr_max=height[0]
        for i in range(n):
            curr_max=max(curr_max,height[i])
            maxl[i]=curr_max
        curr_max=height[n-1]
        for j in range(n-1,-1,-1):
            curr_max=max(curr_max,height[j])
            maxr[j]=curr_max
        res=0
        for i in range(1,n-1):
            res+=(min(maxr[i],maxl[i])-height[i])

        return res





        