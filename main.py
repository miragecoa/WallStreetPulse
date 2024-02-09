from Reddit_Posts import Reddit_Posts

def main():

    posts = Reddit_Posts(num_posts=10,subreddit_name="wallstreetbets")
    posts.posts[0].print_post()



if __name__ == "__main__":
    main()