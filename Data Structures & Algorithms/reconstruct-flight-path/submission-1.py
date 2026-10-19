class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)
        tickets.sort(reverse=True)
        for source, destination in tickets:
            graph[source].append(destination)
        res=[]
        def dfs(node):
            while graph[node]:
                dest=graph[node].pop()
                dfs(dest)
            res.append(node)
            return
        dfs("JFK")
        return res[::-1]
                