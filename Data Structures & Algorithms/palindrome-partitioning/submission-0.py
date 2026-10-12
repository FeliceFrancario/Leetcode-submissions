class Solution:
    def partition(self, s: str) -> List[List[str]]:
        len(s)
        path=[]
        res=[]
        def palindrome(start,end):
            
            while start<=end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
        
        def dfs(i):
            if i==len(s):
                res.append(path.copy())
                return
            for j in range(len(s)-1,i-1,-1):
                if palindrome(i,j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()


        dfs(0)
        return res
        