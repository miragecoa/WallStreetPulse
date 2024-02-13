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

comments = reddit_api.get_post_data("1apwf44")
comments_list = comments.json()
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

# print("Post Text:")
# print(comments_str[0].get('data').get('children')[0].get('data').get('selftext'))

# Direct comments to posts
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
reddit_api.get_comments(comments_list[1])

# Getting the replies of the
# parent_comment = comments_list[1].get('data').get('children')[1].get('data')
# print(comments_list[1].get('data').get('children')[1].get('data').keys())
# # print(comments_list[1].get('data').get('children')[0].get('data').get('replies'))
# # print(type(comments_list[1].get('data').get('children')[0].get('data').get('replies')))
# # print(type(comments_list[1].get('data').get('children')[1].get('data').get('replies')))
# # print(comments_list[1].get('data').get('children')[1].get('data').get('replies').keys())
# # print(comments_list[1].get('data').get('children')[1].get('data').get('replies').get('data'))
# print(parent_comment.get('replies').get('data').keys())
# print(parent_comment.get('replies').get('data').get('children'))
# print(parent_comment.get('replies').get('data').get('children')[0].get('data'))
# print(parent_comment.get('replies').get('data').get('children')[0].get('data').get('body'))