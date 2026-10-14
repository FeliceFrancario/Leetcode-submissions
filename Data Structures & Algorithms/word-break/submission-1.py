class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n=len(s)
        word_set=set(wordDict)
        cache={}
        def dfs(i):
            if i==n:
                return True
            
            if i in cache:
                return cache[i]
            for j in range(i+1,n+1):
                if s[i:j] in word_set and dfs(j):
                    cache[i]=True
                    return True
            cache[i]=False
            return False
        return dfs(0)

        
            


