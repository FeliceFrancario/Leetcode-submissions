class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        H={}
        for n in nums:
            H[n]=1+H.get(n,0)
        
        freq=[[] for _ in range(len(nums)+1)]
        for n,f in H.items():
            freq[f].append(n)
        res=[]
        l=len(freq)-1
        for i in range(l,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res


