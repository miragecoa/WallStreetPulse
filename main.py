import reddit_api
import gpt_api


# Sample usages
posts = reddit_api.get_hot_posts()
print(posts.json())


#response, chat_history = gpt_api.get_response("What is RCOS")

#response, chat_history = gpt_api.get_response("What is WallStreetPulse")





