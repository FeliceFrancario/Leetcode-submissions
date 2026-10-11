class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        one=cost[-2]
        two=cost[-1]
        for i in range(n-3,-1,-1):
            tmp=one
            one=cost[i]+min(one,two)
            two=tmp
        return min(one,two)