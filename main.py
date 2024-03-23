from redditData.reddit_api import Reddit_API

# Reddit API object
# https://www.reddit.com/r/wallstreetbets/comments/1axhn74/most_anticipated_earnings_releases_for_the_week/
api = Reddit_API()
post = api.get_post_data("1axhn74")
hot_posts = api.get_hot_posts()

# Gets all comments and replies for hot posts
# for i in range(0, len(hot_posts.get('data').get('children'))):
#     data = api.get_post_data(api.get_post_id(hot_posts.get('data').get('children')[i]))
#     api.get_comments(data[1])

# api.get_comments(post[1])

# Comments contains a list of directories of comments and replies
comments = []
api.get_dicts(post[1], comments,"1axhn74","1000")
size = len(comments)
# for i in range(0, size):
#     print(comments[i].get('body'))
print(comments[size-1])
print(size)
