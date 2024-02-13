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

def main():
    posts = Reddit_Posts(num_posts=10, subreddit_name="wallstreetbets")
    print(f"Title: {posts.get_title(1)}")
    print(f"Author: {posts.get_author(1)}")
    print(posts.get_content(1))

    print(f"First hot comment: {posts.get_comments(1, 2)[0]['content']}")



if __name__ == "__main__":
    main()