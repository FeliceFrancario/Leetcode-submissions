class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l=0
        res_r=len(s)-1
        res_len=0
        def expandPalindrome(l,r):
            nonlocal res_l,res_r,res_len
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>res_len:
                    res_len=r-l+1
                    res_l=l
                    res_r=r
                l-=1
                r+=1
            
        for i in range(len(s)):
           #r,l=i,i
            expandPalindrome(i,i)
            expandPalindrome(i,i+1)
        return s[res_l:res_r+1]




