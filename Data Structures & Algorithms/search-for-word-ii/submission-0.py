class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
        self.index=-1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows=len(board)
        cols=len(board[0])
        graph=TrieNode()
        for j in range(len(words)):
            curr=graph
            for w in words[j]:
                if w not in curr.children:
                    curr.children[w]=TrieNode()
                curr=curr.children[w]
            curr.end=True
            curr.index=j
        res=[]
        def dfs(r,c,node):
            
            if board[r][c] not in node.children or board[r][c]=='#':
                return 
            char=board[r][c]
            node=node.children[char]
            board[r][c]='#'
            if node.end:
                res.append(words[node.index])
                node.end=False 
            directions=[(1,0),(0,1),(-1,0),(0,-1)]
            for dr, dc in directions:
                nr,nc=dr+r,dc+c
                if 0<=nr<rows and 0<=nc<cols:
                    #tmp=board[nr][nc]
                    dfs(nr,nc,node)
            board[r][c]=char
            return 

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,graph)    

        return res 
                               



        