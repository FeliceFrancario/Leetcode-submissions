class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #l=0
        #r=0
        buy=prices[0]
        #sell=
        profit=0
        for p in prices:
            if p<buy:
                buy=p
                #l+=1
                #r+=1
            elif p>=buy:
                profit=max(profit, p-buy)

        return profit

        