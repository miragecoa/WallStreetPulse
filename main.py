import praw

def authenticate():
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
    return reddit

def print_submission_info(submission):
    print("\nTitle:", submission.title)
    print("Upvotes:", submission.score)

    if submission.selftext:
        print("Content:", submission.selftext)
    elif submission.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        print("Image URL:", submission.url)

def print_top_comments(submission):
    submission.comments.replace_more(limit=0)
    top_comments = submission.comments.list()[:5]

    print("\nTop Comments:")
    for comment in top_comments:
        print(f"{comment.author} ({comment.score} upvotes): {comment.body}")
    print("-" * 100)

def main():
    reddit = authenticate()

    subreddit_name = "wallstreetbets"
    num_posts = 3

    top_posts = reddit.subreddit(subreddit_name).hot(limit=num_posts)

    for submission in top_posts:
        print_submission_info(submission)
        print_top_comments(submission)

if __name__ == "__main__":
    main()