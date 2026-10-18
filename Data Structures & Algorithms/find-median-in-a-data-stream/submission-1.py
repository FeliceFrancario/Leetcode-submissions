class MedianFinder:

    def __init__(self):
        self.H1=[]
        self.H2=[]

    def addNum(self, num: int) -> None:
        if not self.H1 or -num>self.H1[0]:
            heapq.heappush(self.H1,-num)
        else:
            heapq.heappush(self.H2,num)
        while len(self.H1)-len(self.H2)>1:
            val=heapq.heappop(self.H1)
            heapq.heappush(self.H2,-val)
        while len(self.H2)-len(self.H1)>1:
            val=heapq.heappop(self.H2)
            heapq.heappush(self.H1,-val)

    def findMedian(self) -> float:
        if not self.H1 and not self.H2:
            return None
        if len(self.H1)==len(self.H2):
            return (self.H2[0]-self.H1[0])/2
        elif len(self.H1)>len(self.H2):
            return -self.H1[0]
        else:
            return self.H2[0]
        
        