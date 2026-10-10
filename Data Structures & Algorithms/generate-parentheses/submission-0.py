class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path=[]
        res=[]
        def dfs( o, c):
            if o+c==2*n:
                res.append("".join(path))
            
            if o<n:
                path.append("(")
                dfs(o+1,c)
                path.pop()
            if c<o:
                path.append(")")
                dfs(o,c+1)
                path.pop()
        dfs(0,0)
        return res



