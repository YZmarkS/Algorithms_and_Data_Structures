from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.follows = defaultdict(set)
        self.posts_by_users = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts_by_users[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []

        def insert_last_if_non_empty(userId):
            tweet_count = len(self.posts_by_users[userId])
            if tweet_count > 0:
                tweet_time, tweet_id = self.posts_by_users[userId][tweet_count - 1]
                heapq.heappush_max(heap, (tweet_time, tweet_count - 1, userId, tweet_id))

        insert_last_if_non_empty(userId)
        for followee_id in self.follows[userId]:
            insert_last_if_non_empty(followee_id)

        for i in range(10):
            if not heap:
                break
            _, index, user_id, tweet_id = heapq.heappop_max(heap)
            result.append(tweet_id)
            new_index = index - 1
            if new_index >= 0:
                new_tweet_time, new_tweet_id = self.posts_by_users[user_id][new_index]
                heapq.heappush_max(heap, (new_tweet_time, new_index, user_id, new_tweet_id))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
