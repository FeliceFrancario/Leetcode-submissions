class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        #l=n-1
        r=n-1
        for l in range(n-2,-1,-1):
            if nums[l]>=r-l:
                r=l
        return r==0


        