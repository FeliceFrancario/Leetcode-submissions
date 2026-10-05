class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq=set()
        for i in nums:
            if i in uniq:
                return True
            uniq.add(i)

        return False
        


        