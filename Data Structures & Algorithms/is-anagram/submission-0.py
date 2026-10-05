class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_f={}
        for c in s:
            s_f[c]=1+s_f.get(c,0)
        t_f={}
        for c in t:
            t_f[c]=1+t_f.get(c,0)
        if len(s_f) != len(t_f):
            return False
        for k,v in s_f.items():
            if t_f.get(k, 0) != v:
                return False
        return True