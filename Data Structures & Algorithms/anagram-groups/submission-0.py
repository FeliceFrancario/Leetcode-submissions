class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        Dic=defaultdict(list)
        
        for w in strs:
            Arr=[0]*26
            for c in w:
                Arr[ord(c)-ord('a')]+=1
            Dic[tuple(Arr)].append(w)

        return list(Dic.values())
        