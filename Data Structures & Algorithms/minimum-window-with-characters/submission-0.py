class Solution:
    def minWindow(self, s: str, t: str) -> str:
            Hs={}
            Ht={}
            res=""
            minl=0
            #minr=len(s)-1
            minr=0
            minlength=float("inf")
            for c in t:
                Ht[c]=1+Ht.get(c,0)
            #for i in range(len(t)):
            #    Hs[s[i]]=1+Hs.get(s[i],0)
            l=0
            r=0
            #satisfied=False
            need=len(Ht)
            have=0
            while r<len(s):
                c=s[r]
                Hs[c]=1+Hs.get(c,0)
                if c in Ht and Hs[c]==Ht[c]:
                    have+=1
                while have==need:
                    if r-l+1<minlength:
                        minlength=r-l+1
                        minl=l
                        minr=r 
                    Hs[s[l]]-=1
                    if s[l] in Ht and Hs[s[l]]<Ht[s[l]]:
                        have-=1
                    l+=1
                r+=1
            return s[minl:minr+1] if minlength<float('inf') else ""


