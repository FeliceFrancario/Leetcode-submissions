class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}

        def dfs(index,coin):
            if index>=len(prices):
                return 0
            if (index,coin) in memo:
                return memo[(index,coin)]
            if coin:
                memo[(index,coin)]= max(prices[index]+dfs(index+2,0),dfs(index+1,1))
                
            if not coin:
                memo[(index,coin)]=max(dfs(index+1,1)-prices[index], dfs(index+1,0))
            return memo[(index,coin)]

        return dfs(0,0)