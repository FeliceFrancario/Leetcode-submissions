class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph= {i:[] for i in range(1,len(edges)+1)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=set()
        #res=set()
        cycle=set()
        parent_map={}

        def dfs(node,parent):
            if node in visited:
                curr = parent
                while curr != node:
                    cycle.add(curr)
                    curr = parent_map[curr]
                cycle.add(node)
                return True
            visited.add(node)
            parent_map[node]=parent
            for neigh in graph[node]:
                if neigh==parent:
                    continue
                #if neigh in visited:
                #    curr=node
                #    while curr!=neigh:
                #        cycle.add(curr)
                #        curr=parent_map[curr]
                #    cycle.add(neigh)
                #    return True
                if dfs(neigh,node):
                    #parent_map[node]=parent
                    return True

            return False
        dfs(1,-1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]

        

        

        