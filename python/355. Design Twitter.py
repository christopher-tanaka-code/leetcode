from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []

        # User should always see their own tweets
        users = set(self.following[userId])
        users.add(userId)

        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time, tweet_id = self.tweets[uid][idx]

                # Python has min-heap, so use negative time for max-heap behavior
                heapq.heappush(heap, (-time, tweet_id, uid, idx))

        while heap and len(result) < 10:
            neg_time, tweet_id, uid, idx = heapq.heappop(heap)
            result.append(tweet_id)

            # Move to the previous tweet from the same user
            idx -= 1
            if idx >= 0:
                time, prev_tweet_id = self.tweets[uid][idx]
                heapq.heappush(heap, (-time, prev_tweet_id, uid, idx))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)