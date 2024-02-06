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

subreddit_name = "wallstreetbets"
num_posts = 3

top_posts = reddit.subreddit(subreddit_name).hot(limit=num_posts)

# Iterate through each top post
for submission in top_posts:
    print("\nTitle:", submission.title)
    print("Upvotes:", submission.score)

    # Check if the submission has text content
    if submission.selftext:
        print("Content:", submission.selftext)
    # Check if the submission is a link to an image
    elif submission.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        print("Image URL:", submission.url)
               
    
    # Get the top comments for each post
    submission.comments.replace_more(limit=0)
    top_comments = submission.comments.list()[:5]  # Adjust the number as needed
    
    # Print the top comments with upvotes
    print("\nTop Comments:")
    for comment in top_comments:
        print(f"{comment.author} ({comment.score} upvotes): {comment.body}")
    print("-" * 100)
