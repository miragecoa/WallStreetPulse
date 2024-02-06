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

def get_top_posts(subreddit_name, num_posts):
    reddit = authenticate()
    top_posts = reddit.subreddit(subreddit_name).hot(limit=num_posts)
    return sorted(top_posts, key=lambda x: x.score, reverse=True)

def print_submission_info(submission):
    print("\nTitle:", submission.title)
    print("Upvotes:", submission.ups)
    print("Downvotes:", submission.downs)
    
    if submission.selftext:
        print("Content:", submission.selftext)
    elif submission.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        print("Image URL:", submission.url)

def get_top_comments(submission):
    submission.comments.replace_more(limit=0)
    top_comments = sorted(submission.comments.list(), key=lambda x: x.score, reverse=True)[:5]
    return top_comments

def print_top_comments(top_comments):
    print("\nTop Comments:")
    for comment in top_comments:
        print(f"{comment.author} ({comment.score} upvotes, {comment.downs} downvotes): {comment.body}")
    print("-" * 100)

def main():
    subreddit_name = "wallstreetbets"
    num_posts = 3

    top_posts = get_top_posts(subreddit_name, num_posts)

    for submission in top_posts:
        print_submission_info(submission)
        top_comments = get_top_comments(submission)
        print_top_comments(top_comments)

if __name__ == "__main__":
    main()