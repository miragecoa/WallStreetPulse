#import reddit_api
#import gpt_api


# Sample usages
#posts = reddit_api.get_hot_posts()
# print(posts.json())


#response, chat_history = gpt_api.get_response("What is RCOS")

#response, chat_history = gpt_api.get_response("What is WallStreetPulse")


import praw
import time

ID = "mGJKXOitGGulU5pBJ9Zmqg"
SECRIT_KEY = "zZR3V_O4kRdzjJqKZN9-oNluADiHfg"
user = "WallStreetPulse"
PASSWORD = "WSPdevteam"

reddit = praw.Reddit(
    client_id=ID,
    client_secret=SECRIT_KEY,
    username=user,
    password=PASSWORD,
    user_agent="testscript by u/fakebot3",
)

def calculate_score(submission, num_followers):
    weight_posts = 0.3
    weight_followers = 0.2
    weight_upvotes = 0.5

    score = (weight_posts * submission.num_comments + weight_followers * num_followers + weight_upvotes * submission.score)
    return score

start_time = time.time() - 7*24*60*60

for submission in reddit.subreddit("WallStreetbets").top(time_filter="week"):
    if submission.stickied == False and submission.created_utc >= start_time:
        num_followers = submission.author.followers
        score = calculate_score(submission, num_followers)
        print("\nTitle: ", submission.title)
        print("Score: ", score)


#https://praw.readthedocs.io/en/stable/code_overview/models/subreddit.html    #praw.models.Subreddit








