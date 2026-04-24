class Twitter:

    def __init__(self):
        self.tweet_map = defaultdict(list) # max heap (time, userId, tweetId)
        self.follow_lst = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet_map[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        res = []
        if userId not in self.follow_lst[userId]:
            self.follow_lst[userId].add(userId)

        for followee in self.follow_lst[userId]:
            # get the last post the followee posted
            if len(self.tweet_map[followee]) > 0:
                index = len(self.tweet_map[followee]) - 1
                time, tweet = self.tweet_map[followee][index]
                max_heap.append([-time, tweet, followee, index - 1])

        heapq.heapify(max_heap)

        while max_heap and len(res) < 10:
            time, tweet, followee, index = heapq.heappop(max_heap)
            res.append(tweet)

            # next post that that followee posted
            if index >= 0:
                time, tweet = self.tweet_map[followee][index]
                heapq.heappush(max_heap,[-time, tweet, followee, index - 1])
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_lst[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_lst[followerId]:
            self.follow_lst[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)