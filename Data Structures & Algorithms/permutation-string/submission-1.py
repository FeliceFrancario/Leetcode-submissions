class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        l=0
        r=len(s1)
        F1=[0]*26
        F2=[0]*26
        for c in s1:
            F1[ord(c)-ord('a')]+=1
        for i in range(len(s1)):
            F2[ord(s2[i])-ord('a')]+=1

        if F1==F2:
                return True
        while r<len(s2):
            
            
            F2[ord(s2[l])-ord('a')]-=1
            F2[ord(s2[r])-ord('a')]+=1
            l+=1
            r+=1
            if F1==F2:
                return True
        return False
        