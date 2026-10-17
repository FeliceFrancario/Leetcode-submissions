class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c in cur.children:
                cur=cur.children[c]
            else:
                cur.children[c]=TrieNode()
                cur=cur.children[c]
        cur.end=True    

    def search(self, word: str) -> bool:
        #cur=self.root
        return self.dfs(0,self.root,word)


    def dfs(self, index, node,word):
        if index==len(word):
            return node.end
        c=word[index]
        if c=='.':
            for child in node.children:
                if self.dfs(index+1, node.children[child],word):
                    return True
            return False
        else:
            if c not in node.children:
                return False
            #cur=node.children[c]
        return self.dfs(index+1,node.children[c],word)
        
            

