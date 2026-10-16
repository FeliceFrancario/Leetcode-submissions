class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total_sum=sum(nums)
        if total_sum%2:
            return False
        H={}
        target=total_sum/2
        def dfs(idx,curr_sum):
            if curr_sum==target:
                return True
            if curr_sum in H:
                return H[curr_sum]
            if curr_sum>target:
                H[curr_sum]=False
                return False
            for j in range(idx,len(nums)):
                if dfs(j+1,curr_sum+nums[j]):
                    #H[curr_sum+nums[j]]=True
                    return True
            H[curr_sum]=False    
            return False

        return dfs(0,0)

            
            
            
