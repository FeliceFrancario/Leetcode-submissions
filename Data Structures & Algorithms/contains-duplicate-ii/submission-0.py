class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        H=set()
        for r in range(len(nums)):
            if r-l>k:
                H.remove(nums[l])
                l+=1
            if nums[r] in H:
                return True
            else:
                H.add(nums[r])
        return False

        

            
        