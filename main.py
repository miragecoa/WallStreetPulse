from redditData.reddit_api import Reddit_API

# Current Issue:
# I am unable to get replies under the more replies dropdown menu
# can be solved using /api/morechildren

# Reddit API object
# https://www.reddit.com/r/wallstreetbets/comments/1axhn74/most_anticipated_earnings_releases_for_the_week/
api = Reddit_API()
post = api.get_post_data("1axhn74")
hot_posts = api.get_hot_posts()

# For each level of children, add to current level .get('data').get('replies').get('data').get('children')[0]
# Function calls
# print(api.get_post_title(post[0].get('data').get('children')[0]))
# print(api.get_post_content(post[0].get('data').get('children')[0]))
# print(api.get_post_ups(post[0].get('data').get('children')[0]))
# print(api.get_post_downs(post[0].get('data').get('children')[0]))
# print(api.get_post_upvote_ratio(post[0].get('data').get('children')[0]))

# Gets all comments and replies for hot posts
# for i in range(0, len(hot_posts.get('data').get('children'))):
#     data = api.get_post_data(api.get_post_id(hot_posts.get('data').get('children')[i]))
#     api.get_comments(data[1])

res = ""
print(api.get_all_comments_data(post[1], res))
