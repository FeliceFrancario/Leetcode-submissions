class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        memo={}
        def dfs(one,two):
            if one+two>=len(s3):
                return True
            if (one,two) in memo:
                return memo[(one,two)]
            new_one=one
            while new_one<len(s1) and s1[new_one]==s3[new_one+two]:
                new_one+=1
                if dfs(new_one,two):
                    memo[(one,two)]=True
                    return True
            new_two=two
            while new_two<len(s2) and s2[new_two]==s3[one+new_two]:
                new_two+=1
                if dfs(one,new_two):
                    memo[(one,two)]=True
                    return True
            
            memo[(one,two)]=False
            return False

        return dfs(0,0)

            
        