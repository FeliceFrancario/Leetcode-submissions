class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        res=[]
        while nums:
            num=heapq.heappop(nums)
            res.append(num)
        return res