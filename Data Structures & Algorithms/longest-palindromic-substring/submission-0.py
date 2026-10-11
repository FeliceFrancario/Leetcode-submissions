class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l=0
        res_r=len(s)-1
        res_len=0

        for i in range(len(s)):
            r,l=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>res_len:
                    res_len=r-l+1
                    res_l=l
                    res_r=r
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>res_len:
                    res_len=r-l+1
                    res_l=l
                    res_r=r
                l-=1
                r+=1
        return s[res_l:res_r+1]




