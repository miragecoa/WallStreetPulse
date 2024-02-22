from reddit_api import Reddit_API

# Current Issue:
# I am unable to get replies under the more replies dropdown menu
# can be solved using /api/morechildren

# Reddit API object
api = Reddit_API()
post = api.get_post_data("1arusfa")
hot_posts = api.get_hot_posts() # dict
# print(hot_posts.keys()) # dict_keys(['kind', 'data'])
# print(hot_posts.get('data').keys()) # dict_keys(['after', 'dist', 'modhash', 'geo_filter', 'children', 'before'])
# print(hot_posts.get('data').get('children')[0].keys()) # dict_keys(['kind', 'data'])
print(hot_posts.get('data').get('children')[0].get('data').keys())
api.get_all_comments_data(post[1]);

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
