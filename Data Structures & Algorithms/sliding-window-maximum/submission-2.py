class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        res=[]
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        res.append(-heap[0][0])
        for r in range(k,len(nums)):
            heapq.heappush(heap,(-nums[r],r))
            l=r-k
            while heap[0][1]<=l:
                heapq.heappop(heap)
            
            res.append(-heap[0][0])
        return res 
        #can also be done with monotonic decreasing queue. where while last member of queue is smaller we pop. we make sure the left most is the max. plus we just store the indices in the queue. so we can check if l>q[0] popleft().
