class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        uid, tid = userId, tweetId
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = set(self.followees[userId])
        users.add(userId)
        min_heap = []
        for u in users:
            if self.tweets[u]:
                index = len(self.tweets[u]) - 1
                time, tweet_id = self.tweets[u][index]
                heapq.heappush(min_heap, (-time, tweet_id, u, index))
        res = []
        while min_heap and len(res) < 10:
            time, tweet_Id, u, index = heapq.heappop(min_heap)
            res.append(tweet_Id)
            
            if index - 1 >= 0:
                next_time, next_tweet_id = self.tweets[u][index - 1]
                heapq.heappush(min_heap, (-next_time, next_tweet_id, u, index - 1))
            index -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
        
