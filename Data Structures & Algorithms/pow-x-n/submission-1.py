class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n==0:
            return 1
        pos_n=abs(n)
        half=self.myPow(x,pos_n//2)
        res=0
        if pos_n%2:
            res=half*half*x    
        else:
            res=half*half
        return res if n>0 else 1/res

        
