class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        H={}
        def dfs(i):
            if i==0:
                return 0
            if i<0:
                return float("inf")
            if i in H:
                return H[i]
            current_min=float("inf")
            for c in coins:
                if c<=i:
                    current_min=min(current_min, 1+dfs(i-c))

            H[i]=current_min
            return H[i]
        res=dfs(amount)
        return  res if res<float("inf") else -1