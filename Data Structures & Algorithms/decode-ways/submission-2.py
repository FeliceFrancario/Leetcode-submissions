class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        n=len(s)
        prev=1 if s[-1]!='0' else 0
        curr=1
        for i in range(n-2,-1,-1):
            tmp=0
            if s[i]!='0':
                tmp+=curr
            if 10<=int(s[i:i+2])<=26:
                tmp+=prev
            prev=curr
            curr=tmp
        return curr

