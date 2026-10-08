"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        H={}
        def dfs(p):
            if p in H:
                return
            H[p]=Node(p.val)
            for n in p.neighbors:
                dfs(n)
            return
        dfs(node)
        for origin, clone in H.items():
            for origin_neighbours in origin.neighbors:
                clone.neighbors.append(H[origin_neighbours])
        return H[node]
            
        