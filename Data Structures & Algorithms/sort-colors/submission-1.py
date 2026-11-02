class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_num=max(nums)
        min_num=min(nums)
        H={}
        for n in nums:
            H[n]=1+H.get(n,0)
        i=0
        for num in range(min_num,max_num+1):
            while num in H and H[num]>0:
                nums[i]=num
                i+=1
                H[num]-=1
