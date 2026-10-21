class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()#can call sum of squares function and use slow and fast pointer while slow!=fast this way we can find cycle with O(1) space. Right now O(logn) (number of digits in number)
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