class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<nums[r]:
                r=mid
            else:
                l=mid+1
        pivot=r
        
        def binary_search(l,r):
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                if nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return -1
        res=binary_search(0,pivot-1)
        if res!=-1:
            return res
        return binary_search(pivot,len(nums)-1)


        