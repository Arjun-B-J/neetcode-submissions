class Twitter:

    def __init__(self):
        self.count = 0 #here we are interested in recent tweets, so we use a min heap
        self.followerMap = defaultdict(set)
        self.postMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append((self.count,tweetId))
        self.count-=1 #decrement Count as it is shared across the platform as time

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followerMap[userId].add(userId) #user followers themselves
        #fetch all followers last tweet and put them in a minHeap
        minHeap = []
        for followerId in self.followerMap[userId]:
            if followerId in self.postMap: #check if the follower posted anything
                index = len(self.postMap[followerId])-1 #get the last post index
                count,tweetId = self.postMap[followerId][index]
                minHeap.append((count,tweetId,followerId,index-1)) # add the followerId and the next index to be used in case of heappop in the next step
        heapq.heapify(minHeap)
        #build the res, the ones popped , add new ones with the followerId and index
        res = []
        while minHeap and len(res)<10: #and here 
            count,tweetId,followerId,index = heapq.heappop(minHeap) #index is the nextIndex for this follower
            res.append(tweetId)
            if index>=0: #valid index? then get the next post from follower
                count,tweetId = self.postMap[followerId][index]
                heapq.heappush(minHeap,(count,tweetId,followerId,index-1)) #heappush the next tweet

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId) #O(1) we maintain which user followes who all

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]: #if in set remove O(1)
            self.followerMap[followerId].remove(followeeId)
