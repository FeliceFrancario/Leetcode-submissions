class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        H={}
        n=len(nums)
        
        def dfs(i):
            longest=1
            if i==n-1:
                return 1
            if i in H:
                return H[i]
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    longest=max(longest,1+dfs(j))
            H[i]=longest
            return longest

        return max(dfs(i) for i in range(n))