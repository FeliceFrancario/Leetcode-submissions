class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        H={c:i for i,c in enumerate(s)}
        start=0
        end=0
        res=[]
        for i,c in enumerate(s):
            end=max(end,H[c])
            if i==end:
                res.append(end-start+1)
                start=i+1

        return res    