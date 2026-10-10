class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge=""
        l1=0
        l2=0
        while l1<len(word1) and l2<len(word2):
            merge+=word1[l1]
            l1+=1
            merge+=word2[l2]
            l2+=1
        if l1<len(word1):
            merge+=word1[l1:]
        elif l2<len(word2):
            merge+=word2[l2:]
        return merge
        