class Solution:
    def isValid(self, s: str) -> bool:
        forward=['(','{','[']
        backward=[')','{',']']

        Dic={
            ')':'(',
            '}':'{',
            ']':'['

        }
        stack=[]
        if not len(s)//2:
            return False
        for b in s:
            if b in Dic:
                if not stack or not Dic[b]:
                    return False
                val=stack.pop()
                if Dic[b]!=val:
                    return False
                
            if b in Dic.values():
                stack.append(b)
        if stack:
            return False
        
        return True