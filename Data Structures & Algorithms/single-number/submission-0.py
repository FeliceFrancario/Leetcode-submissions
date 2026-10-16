class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t=0
        for n in nums:
            t=t^n
        return t

        