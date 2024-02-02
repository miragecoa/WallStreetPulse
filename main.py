import reddit_api
# import gpt_api


# Sample usages
# posts = reddit_api.get_hot_posts()
# print(posts.json())


# things to get
# title of the post
# comments
# upvote count ups
# downvote count downs
# upvote ratio upvote_ratio
# picture to text?

comments = reddit_api.get_comments("1ah5s7j")
print(comments.json())

# response, chat_history = gpt_api.get_response("What is RCOS")

# response, chat_history = gpt_api.get_response("What is WallStreetPulse")

