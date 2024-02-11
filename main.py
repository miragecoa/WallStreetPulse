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
def printPost(submission):
    print("Title: " + submission.title)
    print("Score: " + submission.score)
    print("Body: " + submission.selftext)
    print("Image URL: " + submission.url)

def main():
    for submission in reddit.subreddit("WallStreetbets").hot(limit=12):
        while(submission.stickied == False):
            continue
        printPost(submission)


#https://praw.readthedocs.io/en/stable/code_overview/models/subreddit.html    #praw.models.Subreddit







