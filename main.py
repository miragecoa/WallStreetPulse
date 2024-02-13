#import reddit_api
#import gpt_api


# Sample usages
#posts = reddit_api.get_hot_posts()
# print(posts.json())


#response, chat_history = gpt_api.get_response("What is RCOS")

#response, chat_history = gpt_api.get_response("What is WallStreetPulse")


import praw

ID = "mGJKXOitGGulU5pBJ9Zmqg"
SECRIT_KEY = "zZR3V_O4kRdzjJqKZN9-oNluADiHfg"
USER_NAME = "WallStreetPulse"
PASSWORD = "WSPdevteam"


reddit = praw.Reddit(
    client_id=ID,
    client_secret=SECRIT_KEY,
    username=USER_NAME,
    password=PASSWORD,
    user_agent="testscript by u/fakebot3",
)

print("Hot Posts:\n")
for submission in reddit.subreddit("WallStreetbets").hot(limit=15):
    print("Score: ")
    print(submission.score)
    print("\n----------------------\n")
    print("Title: ")
    print(submission.title)
    print("\n----------------------\n")
    print("Author: ")
    print(submission.author.name)
    print("\n----------------------\n")
    print("URL: ")
    print(submission.url)
    print("\n----------------------\n")
    print("\n")

print("Rising Posts:\n")
for submission in reddit.subreddit("WallStreetbets").rising(limit=50):
    print("Score: ")
    print(submission.score)
    print("\n----------------------\n")
    print("Title: ")
    print(submission.title)
    print("\n----------------------\n")
    print("Author: ")
    print(submission.author.name)
    print("\n----------------------\n")
    print("URL: ")
    print(submission.url)
    print("\n----------------------\n")
    print("\n")


#https://praw.readthedocs.io/en/stable/code_overview/models/subreddit.html    #praw.models.Subreddit







