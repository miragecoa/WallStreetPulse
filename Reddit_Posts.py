import praw

class Reddit_Comment:
    def __init__(self):
        self.author=""
        self.ups=""
        self.downs=""
        self.content=""
    
    def print_comments(self):
        print(self.author)

class Reddit_Post:
    def __init__(self):
        self.author=""
        self.title=""
        self.content=""
        self.image_urls=[]
        self.ups=""
        self.downs=""
        self.comments=[]
        self.replies=[]
    
    def print_post(self):
        print(self.title)
    
class Reddit_Posts:
    def __init__(self):
        self.posts=[]
    
    def __init__(self,num_posts=10,subreddit_name="wallstreetbets"):
        self.posts=[]

        reddit=self.authenticate()
        
        top_posts = reddit.subreddit(subreddit_name).hot(limit=num_posts)
        top_posts= sorted(top_posts, key=lambda x: x.score, reverse=True)
        
        for submission in top_posts:
            p = Reddit_Post()
            p.author=submission.author
            p.title=submission.title
            p.content=submission.selftext
            p.image_urls=submission.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))
            p.ups=submission.ups
            p.downs=submission.downs
            
            c = Reddit_Comment()
            submission.comments.replace_more(limit=0)
            top_comments = sorted(submission.comments.list(), key=lambda x: x.score, reverse=True)[:5]

            for comment in top_comments:
                c.author=comment.author
                c.ups = comment.score
                c.downs = comment.downs
                c.content = comment.body

                p.comments.append(c)

            self.posts.append(p)
        


    def authenticate(self):
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