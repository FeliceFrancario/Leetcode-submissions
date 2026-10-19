class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        def dfs(index, curr_sum):
            if curr_sum==0:
                return 1
            if index>=len(coins) or curr_sum<0:
                return 0
            if (index,curr_sum) in memo:
                return memo[(index,curr_sum)]
            memo[(index,curr_sum)]=dfs(index,curr_sum-coins[index])+dfs(index+1,curr_sum)
            

            return memo[(index,curr_sum)]


        return dfs(0,amount)