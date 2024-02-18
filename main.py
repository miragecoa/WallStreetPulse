#

#
#
# # Sample usages
# posts = reddit_api.get_hot_posts()
# # print(posts.json())
#
#
# response, chat_history = gpt_api.get_response("What is RCOS")
#
# response, chat_history = gpt_api.get_response("What is WallStreetPulse")
#
#import reddit_api
import gpt_api
import praw
from data import us, blacklist

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


# for submission in reddit.subreddit("WallStreetbets").hot(limit=10):
#     print(submission.title + "\n")
#     submission.comments.replace_more(limit=0)
#     for comment in submission.comments[:5]:
#         print(comment.body)

# Extract tickers from reddit posts and comments
real_ticker_counts = {}
print("-------------------Scanned Reddit Posts-------------------")
for submission in reddit.subreddit("WallStreetbets").hot(limit=10):
    print(submission.title)
    submission.comments.replace_more(limit=10)
    for comment in submission.comments:
        text = comment.body.split()
        possible_ticker = [word for word in text if word.isupper() and len(word) <= 5]
        for ticker in possible_ticker:
            if ticker not in blacklist and ticker in us:
                if ticker in real_ticker_counts:
                    real_ticker_counts[ticker] += 1
                else:
                    real_ticker_counts[ticker] = 1
print("-----------------Scanned Reddit Posts End-----------------\n")
# # Count number of tickers in each comment
# ticker_counts = {}
# for ticker in real_tickers:
#     if ticker in ticker_counts:
#         ticker_counts[ticker] += 1
#     else:
#         ticker_counts[ticker] = 1

sorted_tickers = sorted(real_ticker_counts.items(), key=lambda x: x[1], reverse=True)
print("Top 10 discussed tickers:")
for ticker in sorted_tickers[:10]:
    print(ticker)

#https://praw.readthedocs.io/en/stable/code_overview/models/subreddit.html    #praw.models.Subreddit