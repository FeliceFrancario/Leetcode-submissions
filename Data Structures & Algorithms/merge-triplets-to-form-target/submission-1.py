class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        
        #one,two,three=False,False,False
        max_vals=[0,0,0]
        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            max_vals=[max(max_vals[i],t[i]) for i in range(3)]
        return max_vals==target

            