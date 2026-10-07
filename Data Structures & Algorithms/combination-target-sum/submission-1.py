class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        nums.sort(reverse=True)
        def dfs(i, curr_sum):

            if curr_sum>target:
                return None
            if curr_sum==target:
                res.append(path.copy())
                return
            for j in range(i,len(nums)):
                path.append(nums[j])
                dfs(j,curr_sum+nums[j])
                path.pop()
            return res
        return dfs(0,0)