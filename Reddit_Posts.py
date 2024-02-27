import praw
from collections import Counter
from datetime import datetime, timedelta

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
    
    def get_user_post_frequency(self, username, time_frame_days):
        # Calculate the timestamp for the specified time frame
        timestamp_limit = datetime.utcnow() - timedelta(days=time_frame_days)
        timestamp = int(timestamp_limit.timestamp())

        # Extract the authors from the posts using the get_author method and filter by time frame
        posts_within_time_frame = [post for post in self.posts if
                                   post.created_utc > timestamp and post.author and post.author.name == username]

        # Count the frequency of posts for the specified user
        user_frequency = len(posts_within_time_frame)

        return user_frequency
    
    def get_all_authors_post_frequency(self, time_frame_days):
        # Calculate the timestamp for the specified time frame
        timestamp_limit = datetime.utcnow() - timedelta(days=time_frame_days)
        timestamp = int(timestamp_limit.timestamp())

        # Extract the authors from the posts using the get_author method and filter by time frame
        authors = [post.author.name for post in self.posts if
                   post.created_utc > timestamp and post.author is not None]

        # Count the frequency of posts for each author
        author_frequency = Counter(authors)

        return dict(author_frequency)
    
    ### Updated Method ###
    # Calculate the post frequency, average upvotes per post, upvote to downvote ratio per post,
    # and average comments per post for each unique author in the specified time frame
    def get_all_authors_post_stats(self, time_frame_days):
        # Calculate the timestamp for the specified time frame
        timestamp_limit = datetime.utcnow() - timedelta(days=time_frame_days)
        timestamp = int(timestamp_limit.timestamp())
        # Initialize dictionaries to store post statistics for each author
        author_frequency = Counter()
        author_upvotes = Counter()
        author_downvotes = Counter()
        author_comments = Counter()
        # Iterate through posts and calculate post statistics for each author
        for post in self.posts:
            if post.created_utc > timestamp and post.author is not None:
                author_frequency[post.author.name] += 1
                author_upvotes[post.author.name] += post.ups
                author_downvotes[post.author.name] += post.downs
                author_comments[post.author.name] += post.num_comments + len(post.comments.list())

        # Calculate average upvotes per post, upvote to downvote ratio per post,
        # and average comments per post for each author
        author_average_upvotes = {author: (upvotes / frequency) if frequency > 0 else 0
                                  for author, frequency in author_frequency.items()
                                  for upvotes in [author_upvotes[author]]}
        
        author_upvote_to_downvote_ratio = {author: (upvotes / max(downvotes, 1))  # Avoid division by zero
                                           for author, upvotes in author_upvotes.items()
                                           for downvotes in [author_downvotes[author]]}

        author_average_comments = {author: (comments / frequency) if frequency > 0 else 0
                                   for author, frequency in author_frequency.items()
                                   for comments in [author_comments[author]]}

        return dict(author_frequency), author_average_upvotes, author_upvote_to_downvote_ratio, author_average_comments

    weights = {
        'frequency': 0.2,
        'upvotes': 0.4,
        'ratio': 0.3,
        'comments': 0.1
    }

    def calculate_author_scores(self, authors_frequency, authors_average_upvotes, authors_upvote_to_downvote_ratio, authors_average_comments):
        author_scores = {}

        for author in authors_frequency.keys():
            # Calculate scores for each criterion
            frequency_score = authors_frequency[author] * self.weights.get('frequency', 1)
            upvotes_score = authors_average_upvotes.get(author, 0) * self.weights.get('upvotes', 1)
            ratio_score = authors_upvote_to_downvote_ratio.get(author, 0) * self.weights.get('ratio', 1)
            comments_score = authors_average_comments.get(author, 0) * self.weights.get('comments', 1)

            # Combine scores using weights
            total_score = frequency_score + upvotes_score + ratio_score + comments_score

            # Store the total score for the author
            author_scores[author] = total_score

        return author_scores
    
    def get_top_authors_info(self, time_frame_days, num_comments):
    # Get post statistics and author scores
        authors_frequency, authors_average_upvotes, authors_upvote_to_downvote_ratio, authors_average_comments = self.get_all_authors_post_stats(time_frame_days)

        # Calculate author scores
        author_scores = self.calculate_author_scores(authors_frequency, authors_average_upvotes, authors_upvote_to_downvote_ratio, authors_average_comments)

        # Sort authors based on their scores (descending order)
        sorted_authors = sorted(author_scores.items(), key=lambda x: x[1], reverse=True)

        # Take the top 10 authors
        top_authors = sorted_authors[:10]

        # Gather information for each top author
        author_info = []
        for author, _ in top_authors:
            # Get titles, content, comments, and replies
            posts_info = []
            for post_index in range(len(self.posts)):
                title = self.get_title(post_index)
                content = self.get_content(post_index)
                author_name = self.get_author(post_index)  # Get the author name for the current post
                comments = self.get_comments(post_index, num_comments)
                comment_data = []
                for comment_info in comments:
                    comment_data.append({
                        'author': comment_info['author'],
                        'upvotes': comment_info['upvotes'],
                        'downvotes': comment_info['downvotes'],
                        'content': comment_info['content'],
                        'replies': comment_info['replies']
                    })
                posts_info.append({
                    'title': title,
                    'content': content,
                    'author': author_name,  # Store the author name for the current post
                    'comments': comment_data
                })

            # Store the information in a dictionary
            author_info.append({
                'author': author,
                'posts': posts_info
            })

        return author_info
    
    
    
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
        post = self.posts[n]
    # Check if the post is a text post
        if post.is_self:
            return post.selftext
        # Check if the post is an image post
        elif post.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            return f"Image URL: {post.url}"
        # Return None for other types of posts
        else:
            return None

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
        post = self.posts[n]
        post.comments.replace_more(limit=0)
        comments = sorted(post.comments.list(), key=lambda x: x.score, reverse=True)[:num_comments]

        comment_data = []
        for comment in comments:
            # comment_info is a dictionary containing information about the comment,
            # including the author, upvotes, downvotes, content, and replies.
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
