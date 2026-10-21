class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        graph={c:set() for w in words for c in w}
        #first=words[0]
        for i in range(1,len(words)):
            minlength=min(len(words[i-1]),len(words[i]))
            if len(words[i-1])>len(words[i]) and words[i-1][:minlength]==words[i][:minlength]:
                return ""
            for j in range(minlength):
                if words[i][j]!=words[i-1][j]:
                    graph[words[i-1][j]].add(words[i][j])
                    break
                
        visited=set()
        cycle=set()
        res=[]
        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            visited.add(c)
            cycle.add(c)
            for nei in graph[c]:
                if not dfs(nei):
                    return False
                    
            cycle.remove(c)
            res.append(c)
            return True

        for c in graph:
            if not dfs(c):
                return ""
        return "".join(res[::-1])

            
            