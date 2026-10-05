class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        uniq=set()
        l=0
        r=0
        for c in s:
            while c in uniq:
                uniq.remove(s[l])
                l+=1
            uniq.add(c)
            length=max(length,r-l+1)
            r+=1
        return length

        