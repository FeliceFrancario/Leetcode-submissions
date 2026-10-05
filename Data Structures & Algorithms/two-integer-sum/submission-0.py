class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H={}
        for i,n in enumerate(nums):
            if n in H:
                return [H[n],i]

            diff=target-n
            H[diff]=i


        