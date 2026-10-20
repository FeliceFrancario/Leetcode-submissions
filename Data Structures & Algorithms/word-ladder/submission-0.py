class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        graph=defaultdict(list)
        wordList.append(beginWord)
        N=len(wordList)
        word_length=len(wordList[0])
        for w in wordList:
            for swap in range(word_length):
                word=""
                for i in range(word_length):
                    if i==swap:
                        word+="*"
                        continue
                    word+=w[i]
                
                graph[word].append(w)

        visited=set([beginWord])
        queue=deque([beginWord])
        res=1
        while queue:
            for i in range(len(queue)):
                curr_word=queue.popleft()
                if curr_word==endWord:
                    return res
                for j in range(word_length):
                    pattern=curr_word[:j]+"*"+curr_word[j+1:]
                    for neigh in graph[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            queue.append(neigh)
            res+=1
        return 0


