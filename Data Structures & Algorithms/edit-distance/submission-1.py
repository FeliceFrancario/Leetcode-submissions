class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1=len(word1)
        len2=len(word2)
        #if len1<len2:
        #    word1,word2=word2,word1
        memo={}
        def dfs(i1,i2):
            if i1==len1:
                return len2-i2
            if i2==len2:
                return len1-i1

            if (i1,i2) in memo:
                return memo[(i1,i2)]
            res=dfs(i1+1,i2+1)
            if word1[i1]!=word2[i2]:
                res=1+min(dfs(i1+1,i2),dfs(i1,i2+1),res)
            memo[(i1,i2)]=res

            return res
        return dfs(0,0)
        