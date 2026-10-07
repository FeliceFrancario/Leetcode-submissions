class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        H={}
        l=len(nums)
        max_num=0
        for n in nums:
            H[n]=1+H.get(n,0)
            max_num=max(max_num,H[n])
            if max_num>l//2:
                return n

        
        