class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]

        dp=[[-1]*len(nums) for _ in range(len(nums))]


        def dfs(l,r):
            if l>r:
                return 0
            if dp[l][r]!=-1:
                return dp[l][r]
            #we are gonna go from the last member popped and add by recursion the values from the 2 subsequence on the side. since if its the last popped the 2 subsequence will never be connected so they can be independent
            for i in range(l,r+1):
                coins=nums[i]*nums[l-1]*nums[r+1]
                coins+=dfs(l,i-1) + dfs(i+1,r)
                dp[l][r]=max(dp[l][r],coins)#max value of every possible pop position
                #O(n^3) time complexity and O(n^2) space complexity
            
            return dp[l][r]

        return dfs(1,len(nums)-2)#because we padded extra 1 on both sides
