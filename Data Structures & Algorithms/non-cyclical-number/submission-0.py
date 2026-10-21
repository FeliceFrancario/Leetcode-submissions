class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        while True:
            res=0
            while n!=0:
                digit=n%10
                n=n//10
                res+=digit*digit
            n=res
            
            if n==1:
                return True
            if n in visited:
                return False
            visited.add(n)