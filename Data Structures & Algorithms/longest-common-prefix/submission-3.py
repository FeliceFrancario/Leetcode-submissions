class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ref=strs[0]
        for i in range(len(ref)):
            for s in strs:
                if i==len(s) or s[i]!=ref[i]:
                    return s[:i]
        return strs[0]


        