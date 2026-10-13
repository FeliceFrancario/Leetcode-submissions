class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curr_max=1
        curr_min=1
        res=max(nums)
        for n in nums:
            #tmp=curr_max
            curr_max,curr_min=max(n,n*curr_max,n*curr_min),min(n,n*curr_max,n*curr_min)
            res=max(res,curr_max)
        return res
