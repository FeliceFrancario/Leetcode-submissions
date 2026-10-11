class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def linear_rob(l,r):
            if l==r:
                return nums[l]
            one=0
            two=0
            for i in range(l,r+1):
                tmp=two
                two=max(two,one+nums[i])
                one=tmp
            return two
        return max(linear_rob(1,n-1), linear_rob(0,n-2))

