import jsonHelper
from gpt_api import get_response
from redditData.Reddit_Posts import Reddit_Posts
from datetime import datetime, timedelta

def analyze_and_record_posts(subreddit_name):
    posts = Reddit_Posts(num_posts=50, subreddit_name=subreddit_name)
    for post in posts:
        # Check if the post has already been analyzed (not sure how this is implemented in project)
        if not jsonHelper.check_if_post_exists(post.id):
            # Use GPT to identify what the post is about
            post_theme, _ = get_response(post.title + " " + post.selftext)

            # Check support of comments
            supportive_comments = 0
            total_comments = len(post.comments)
            for comment in post.comments:
                sentiment, _ = get_response(comment.body)
                if "supportive" in sentiment:
                    supportive_comments += 1

            # Calculate support ratio
            support_ratio = supportive_comments / total_comments if total_comments > 0 else 0

            # Record the analysis results in the database (not sure how this is done currently)
            jsonHelper.add_post()
            print(f"Analyzed and recorded post {post.id}: Theme - {post_theme}, Support Ratio - {support_ratio}")
