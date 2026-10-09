class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        H=set(nums)
        maxl=0
        for n in H:
            if n-1 not in H:
                l=1
                while n + l in H:
                    l+=1
                maxl=max(l,maxl)
        return maxl