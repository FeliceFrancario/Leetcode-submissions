class Twitter:

    def __init__(self):
        self.tweets=defaultdict(list)
        self.followers=defaultdict(set)
        self.count=0
        #self.feed=[]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count,tweetId))
        self.count-=1
        #heapq.heappush((-count,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:

        res=[]
        heap=[]
        self.followers[userId].add(userId)
        
        for f in self.followers[userId]:
            if f in self.tweets:
                index=len(self.tweets[f])-1
                count, tweetId=self.tweets[f][index]
                heap.append([count,tweetId,f,index-1])
    
        heapq.heapify(heap)
        while heap and len(res)<10:
            count,tweetId, followeeId,index=heapq.heappop(heap)
            res.append(tweetId)
            if index>=0:
                count, tweetId=self.tweets[followeeId][index]
                heapq.heappush(heap,[count,tweetId,followeeId,index-1])
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
