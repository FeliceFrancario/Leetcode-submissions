class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph={i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=set()

        def dfs(node, parent):
            if node in visited:
                return 0
            visited.add(node)
            for nei in graph[node]:
                if nei==parent:
                    continue
                dfs(nei,node)
            return 1
        
        count=0
        for i in range(n):
            count+=dfs(i,-1)
        return count


