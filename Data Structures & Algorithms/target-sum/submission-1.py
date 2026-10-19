class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        memo={}
        def dfs(index, curr_sum):
            if index==len(nums) and curr_sum==0:
                return 1
            if index>=len(nums):
                return 0
            if (index,curr_sum) in memo:
                return memo[(index,curr_sum)]
            memo[(index,curr_sum)]=dfs(index+1,curr_sum-nums[index])+dfs(index+1,curr_sum+nums[index])

            return memo[(index,curr_sum)]
        return dfs(0,target)
