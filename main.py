'''
import reddit_api
import gpt_api


# Sample usages
posts = reddit_api.get_hot_posts()
# print(posts.json())


response, chat_history = gpt_api.get_response("What is RCOS")

response, chat_history = gpt_api.get_response("What is WallStreetPulse")
'''

from Reddit_Posts import Reddit_Posts
from datetime import datetime, timedelta

def main():
    posts = Reddit_Posts(num_posts=100, subreddit_name="wallstreetbets")
    '''
    ###test to see posts titles, authors, and comments works
    print(f"Title: {posts.get_title(1)}")
    print(f"Author: {posts.get_author(1)}")
    print(posts.get_content(2))
    print(f"First hot comment: {posts.get_comments(1, 1)[0]['content']}")

    ###test to see if a specific user's post frequency is correct
    username_to_check = "OPINION_IS_UNPOPULAR"
    frequency_for_user = posts.get_user_post_frequency(username_to_check, time_frame_days)
    print(f"The frequency of posts by {username_to_check} in the chosen subreddit in the last {time_frame_days} days is: {frequency_for_user}")
    posts_titles_within_time_frame = [post.title for post in posts.posts if
                                      post.created_utc > timestamp_limit.timestamp() 
                                      and post.author and post.author.name == username_to_check]
    print(f"Titles of posts by {username_to_check} in the last {time_frame_days} days:")
    for title in posts_titles_within_time_frame:
        print(f"- {title}")
    
    ###test to see every author's posts that we grab from the desired number of votes
    time_frame_days = 3
    authors_frequency = posts.get_all_authors_post_frequency(time_frame_days)
    timestamp_limit = datetime.utcnow() - timedelta(days=time_frame_days)

    # Print the results
    for author, frequency in authors_frequency.items():
        print(f"The frequency of posts by {author} in the chosen subreddit in the last {time_frame_days} days is: {frequency}")

        # Print titles of posts by the specified author within the time frame
        posts_titles_within_time_frame = [post.title for post in posts.posts if
                                           post.created_utc > timestamp_limit.timestamp() and
                                           post.author and
                                           post.author.name == author]
        print(f"Titles of posts by {author} in the last {time_frame_days} days:")
        for title in posts_titles_within_time_frame:
            print(f"- {title}")
    
    ###test to see if all post stats are correct
    time_frame_days = 3
    # Get the timestamp for the start of the time frame
    timestamp_limit = datetime.utcnow() - timedelta(days=time_frame_days)

    # Get post frequency, average upvotes per post, upvote to downvote ratio per post,
    # and average comments per post for each unique author in the specified time frame
    authors_frequency, authors_average_upvotes, authors_upvote_to_downvote_ratio, authors_average_comments = posts.get_all_authors_post_stats(time_frame_days)

    # Print the results
    for author, frequency in authors_frequency.items():
        print(f"The frequency of posts by {author} in the chosen subreddit in the last {time_frame_days} days is: {frequency}")

        # Print average upvotes per post for each author
        average_upvotes = authors_average_upvotes.get(author, 0)
        print(f"The average upvotes per post for {author} in the last {time_frame_days} days is: {average_upvotes}")

        # Print upvote to downvote ratio per post for each author
        upvote_to_downvote_ratio = authors_upvote_to_downvote_ratio.get(author, 0)
        print(f"The upvote to downvote ratio per post for {author} in the last {time_frame_days} days is: {upvote_to_downvote_ratio}")

        # Print average comments per post for each author
        average_comments = authors_average_comments.get(author, 0)
        print(f"The average comments per post for {author} in the last {time_frame_days} days is: {average_comments}")
    '''
    time_frame_days = 3
    # Get post frequency, average upvotes per post, upvote to downvote ratio per post,
    # and average comments per post for each unique author in the specified time frame
    authors_frequency, authors_average_upvotes, authors_upvote_to_downvote_ratio, authors_average_comments = posts.get_all_authors_post_stats(time_frame_days)

   
    author_scores = posts.calculate_author_scores(authors_frequency, authors_average_upvotes, authors_upvote_to_downvote_ratio, authors_average_comments)

    # Print the composite scores
    for author, score in author_scores.items():
        print(f"The composite score for {author} is: {score}")

if __name__ == "__main__":
    main()