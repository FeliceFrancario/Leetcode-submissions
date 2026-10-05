class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uniq=set(s)
        rep=0
        length=0
        for c in uniq:
            count=l=0
            for r in range(len(s)):
                if s[r]==c:
                    count+=1
                #if s[r]!=c and rep<k:
                #    rep=rep+1
                #while rep>=k: 
                #    l+=1
                while (r-l+1)-count>k:
                    if s[l]==c:
                        count-=1
                    l+=1
                length=max(length,r-l+1)
        return length


            





        