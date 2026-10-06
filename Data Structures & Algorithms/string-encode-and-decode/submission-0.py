class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=""
        for s in strs:
            enc+=str(len(s))+'#'+ s
        return enc

        
    def decode(self, s: str) -> List[str]:
        l=0
        dec=[]
        while l<len(s):
            j=l
            while s[j]!='#':
                j+=1
            length=int(s[l:j])
            dec.append(s[j+1:j+1+length])
            l= j+1+length
        return dec
