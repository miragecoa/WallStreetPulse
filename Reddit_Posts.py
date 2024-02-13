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

class Reddit_Posts:
    def __init__(self, num_posts=10, subreddit_name="wallstreetbets"):
        posts = reddit.subreddit(subreddit_name).hot(limit=num_posts)
        # !!!!!self.posts sorting by score takes long time
        print("Blocking on Generating posts")
        # unsorted hotpost
        self.posts = list(posts)
        # sorted hotpost
        # self.posts = sorted(posts, key=lambda x: x.score, reverse=True)
        print("Release")

    ### Specification ###
    # inputs:
    #   n: the number of the post
    # return: the author name of the n-th post
    # String
    def get_author(self, n):
        return self.posts[n].author

    ### Specification ###
    # inputs:
    #   n: the number of the post
    # return: the title of the n-th post
    # String
    def get_title(self, n):
        return self.posts[n].title

    ### Specification ###
    # inputs:
    #   n: the number of the post
    # return: the content of the n-th post (What the author says)
    # String
    def get_content(self, n):
        return self.posts[n].selftext

    ### Specification ###
    # inputs:
    #   n: the number of the post
    # return: the content of the n-th post (What the author says)
    # List of String.   ["urls","urls"]
    def get_images(self, n):
        return self.posts[n].url.endswith(('.jpg', '.jpeg', '.png', '.gif'))

    ### Specification ###
    # inputs:
    #   n: the number of the post
    # return: the upvotes of the n-th post
    # String
    def get_upvotes(self, n):
        return self.posts[n].ups

    ### Specification ###
    # inputs:
    #   n: the number of the post
    # return: the downvotes of the n-th post
    # String
    def get_downvotes(self, n):
        return self.posts[n].downs

    ### Specification ###
    # inputs:
    #   n: the number of the post
    #   num_comments: number of top comments you want under that post
    # return: the comments of the n-th post
    # List of Comments Object
    #
    # These are elements inside comment (could be more)
    # comment.author
    # comment.body
    # comment.score
    # comment.downs
    def get_comments(self, n, num_comments):
        self.posts[n].comments.replace_more(limit=0)
        comments = sorted(self.posts[n].comments.list(), key=lambda x: x.score, reverse=True)[:num_comments]

        comment_data = []
        for comment in comments:
            comment_info = {
                'author': comment.author,
                'upvotes': comment.score,
                'downvotes': comment.downs,
                'content': comment.body,
                'replies': self.get_comment_replies(comment, num_replies=3)  # Adjust the number of replies as needed
            }
            comment_data.append(comment_info)

        return comment_data

    def get_comment_replies(self, comment, num_replies):
        comment.replies.replace_more(limit=0)
        replies = comment.replies.list()[:num_replies]

        reply_data = []
        for reply in replies:
            reply_info = {
                'author': reply.author,
                'upvotes': reply.score,
                'downvotes': reply.downs,
                'content': reply.body
            }
            reply_data.append(reply_info)

        return reply_data
