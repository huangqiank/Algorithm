
###355. 设计推特
#设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，
# 能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：
#postTweet(userId, tweetId): 创建一条新的推文
#getNewsFeed(userId): 检索最近的十条推文。
# 每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
#follow(followerId, followeeId): 关注一个用户
#unfollow(followerId, followeeId): 取消关注一个用户
#示例:
#Twitter twitter = new Twitter();
#// 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
#twitter.postTweet(1, 5);
#// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
#twitter.getNewsFeed(1);
#// 用户1关注了用户2.
#twitter.follow(1, 2);
#// 用户2发送了一个新推文 (推文id = 6).
#twitter.postTweet(2, 6);
#// 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
#// 推文id6应当在推文id5之前，因为它是在5之后发送的.
#twitter.getNewsFeed(1);
#// 用户1取消关注了用户2.
#twitter.unfollow(1, 2);
#// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
#// 因为用户1已经不再关注用户2.
#twitter.getNewsFeed(1);

## (1,5) (2,6)
# [1,2]
## follow_dict = {}
## user_tweet = {}
## twwet_time [ ]
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follow_dict=  {}
        self.user_tweet= {}
        self.tweet_time = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.user_tweet:
            self.user_tweet[userId] = {tweetId}
        else:
            self.user_tweet[userId].add(tweetId)
        n = len(self.tweet_time)
        self.tweet_time[tweetId] = n+1

    def getNewsFeed(self, userId) :
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        all_user=[userId]
        all_tweet = []
        if userId in self.follow_dict:
            for i in self.follow_dict[userId]:
                all_user.append(i)
        for i in all_user:
            if i in self.user_tweet:
                for j in self.user_tweet[i]:
                    all_tweet.append((j,self.tweet_time[j]))
        res= sorted(all_tweet, key = lambda x:x[1],reverse=True)
        ans = []
        count =0
        for i in res:
            if count <10:
                ans.append(i[0])
            count+=1
        return ans[:10]


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follow_dict:
            self.follow_dict[followerId] = {followeeId}
        else:
            self.follow_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follow_dict:
            return
        if followeeId in self.follow_dict[followerId]:
            self.follow_dict[followerId].remove(followeeId)
        return

