class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        rank=[1]*(n+1)


        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            rootx=find(x)
            rooty=find(y)

            if rootx==rooty:
                return False
            
            if rank[rootx]>rank[rooty]:
                rank[rootx]+=rank[rooty]
                parent[rooty]=rootx
            else:
                rank[rooty]+=rank[rootx]
                parent[rootx]=rooty
            return True
        for u, v in edges:
            if not union(u,v):
                return [u,v]
        return []
        

        

        