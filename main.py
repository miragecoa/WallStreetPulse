from reddit_api import Reddit_API
# import gpt_api

# Reddit API object
api = Reddit_API()
post = api.get_post_data("1asbggq")

# Current Issue:
# I am unable to get replies under the more replies dropdown menu
# can be solved using /api/morechildren
