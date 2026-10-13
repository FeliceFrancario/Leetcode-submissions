class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq={}
        for t in tasks:
            freq[t]=1+freq.get(t,0)
        heap=[]
        for t in freq:
            heap.append((-freq[t],t))
        heapq.heapify(heap)

        queue=deque([])
        time=0
        while heap or queue:
            time+=1
            if heap:
                f,t=heapq.heappop(heap)
                if f+1<0:
                    queue.append([time+n,(f+1,t)])#f+1 because f is negative
            #else:
            #    time=queue[0][0]
            if queue and time>=queue[0][0]:
                _,pair=queue.popleft()
                heapq.heappush(heap,pair)
        return time
        