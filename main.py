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

comments = reddit_api.get_comments("1akcxex")
comments_str = comments.json()

# print(comments_str[0].get('data'))
# print(comments_str[0].get('data').keys())
# print(comments_str[0].get('data').get('children'))
# print(type(comments_str[0].get('data').get('children')))
# print("Break")
# print(comments_str[0].get('data').get('children'))
# print(type(comments_str[0].get('data').get('children')[0]))
# print(comments_str[0].get('data').get('children')[0].keys())
#
# print(comments_str[0].get('data').get('children')[0].get('data'))
# print(type(comments_str[0].get('data').get('children')[0].get('data')))
#
# print(comments_str[0].get('data').get('children')[0].get('data').keys())

print("Post Text:")
print(comments_str[0].get('data').get('children')[0].get('data').get('selftext'))

# print(type(comments_str[1]))
# print(comments_str[1].keys())
# print(comments_str[1].get('data'))
# print(type(comments_str[1].get('data')))
# print(comments_str[1].get('data').keys())
# print(comments_str[1].get('data').get('children'))
# print(type(comments_str[1].get('data').get('children')))
# print(type(comments_str[1].get('data').get('children')[0]))
# print(comments_str[1].get('data').get('children')[0].keys())
# print(comments_str[1].get('data').get('children')[0].get('data'))
# print(type(comments_str[1].get('data').get('children')[0].get('data')))
# print(comments_str[1].get('data').get('children')[0].get('data').keys())

print("Comments:")
# print(comments_str[1].get('data').get('children')[0].get('data').get('body'))
for i in range(1, len(comments_str[1].get('data').get('children'))):
    print(comments_str[1].get('data').get('children')[i].get('data').get('body'))


# response, chat_history = gpt_api.get_response("What is RCOS")

# response, chat_history = gpt_api.get_response("What is WallStreetPulse")

