class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo={}
        s_len=len(s)
        t_len=len(t)

        def dfs(s_index,t_index):

            if t_index==t_len:
                return 1
            if s_index==s_len:
                return 0
            if (s_index,t_index) in memo:
                return memo[(s_index,t_index)]
            proceed=0
            if s[s_index]==t[t_index]:
                proceed=dfs(s_index+1,t_index+1)
            memo[(s_index,t_index)]=proceed+dfs(s_index+1,t_index)


            return memo[(s_index,t_index)]

        return dfs(0,0)
