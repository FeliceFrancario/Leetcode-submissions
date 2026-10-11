class Solution:
    def rob(self, nums: List[int]) -> int:
        H={}
        n=len(nums)
        def dfs(i):
            nonlocal H
            if i>=n:
                return 0
            if i in H:
                return H[i]
            H[i]= max(nums[i]+dfs(i+2),dfs(i+1))
            return H[i]
        return dfs(0)    