import requests
# Setting up authorization header
ID = "mGJKXOitGGulU5pBJ9Zmqg"
SECRET_KEY = "zZR3V_O4kRdzjJqKZN9-oNluADiHfg"
auth = requests.auth.HTTPBasicAuth(ID, SECRET_KEY)

with open('pswd.txt', 'r') as f:
    pswd = f.read()

data = {
    'grant_type': 'password',
    'username': 'WallStreetPulse',
    'password' : pswd
}

headers = {'User-Agent': "WallStreetPulse/0.0.1"}
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}'
BASE_URL = 'https://oauth.reddit.com/r/wallstreetbets'

# things to get
# title of the post // Done
# comments // Done (issue with scope)
# upvote count ups // Done
# downvote count downs // Done
# upvote ratio upvote_ratio // Done
# picture to text?

class Reddit_API:
    def __init__(self):
        self.client_id = ID
        self.secret_key = SECRET_KEY
        self.auth = auth
        self.data = data
        self.headers = headers
        self.token = TOKEN

    # Gets hot posts
    def get_hot_posts(self):
        return requests.get(BASE_URL + "/hot", headers=headers).json()

    # post should be in this format json.get('data').get('children')[i]
    def get_post_id(self, post):
        return post.get('data').get('id')

    # Returns a list containing the data of the post
    def get_post_data(self, id):
        return requests.get(BASE_URL + "/comments/" + id, headers=headers).json()

    # Get the title of the post
    def get_post_title(self, data):
        return data.get('data').get('title')

    # Returns the content in the post
    def get_post_content(self, data):
        return data.get('data').get('selftext')

    # Gets the ups of a post/comment
    def get_ups(self, data):
        return data.get('data').get('ups')

    # Gets the downs of a post/comment
    def get_downs(self, data):
        return data.get('data').get('downs')

    # Gets the upvote ratio of a post/comment
    def get_upvote_ratio(self, data):
        return data.get('data').get('upvote_ratio')

    # Gets a comment and all its replies on a post
    # comment should be in format post[1].get('data').get('children')[i]
    def get_comment(self, comment):
        return comment.get('data').get('body')

    # Gets comments, replies and individual ups, downs, and upvote ratio.
    def get_all_comments_data(self, data, res):  # make this return a string
        for i in range(0, len(data.get('data').get('children'))):
            res = (res + f"{self.get_comment(data.get('data').get('children')[i])}"
                   + " Ups: " + f"{self.get_ups(data.get('data').get('children')[i])}"
                   + " Downs: " + f"{self.get_downs(data.get('data').get('children')[i])}"
                   + " Ratio: " + f"{self.get_upvote_ratio(data.get('data').get('children')[i])}" + "\n")
            # Print all data of the replies to the comment
            if isinstance(data.get('data').get('children')[i].get('data').get('replies'), dict):
                self.get_all_comments_data(data.get('data').get('children')[i].get('data').get('replies'), res)
        return res

    # FUNCTIONS FOR TESTING
    # Gets all data for the post for testing
    def get_all_post_data(self, data):
        print(self.get_post_title(data))
        print(self.get_post_content(data))
        print(self.get_ups(data))
        print(self.get_downs(data))
        print(self.get_upvote_ratio(data))

    # Gets all comments and all replies to a comment of a post for testing
    # data should be in format post[1]
    def get_comments(self, data):
        # Prints the direct comments of the post
        for i in range(0, len(data.get('data').get('children'))):
            print(self.get_comment(data.get('data').get('children')[i]))
            # Print all replies to the comment
            if isinstance(data.get('data').get('children')[i].get('data').get('replies'), dict):
                self.get_comments(data.get('data').get('children')[i].get('data').get('replies'))

    def get_more_children(self, comment_id, link_id, children, limit, depth):
        params = {
            'link_id': link_id,
            'children': children,
            'limit_children': limit,
            'depth': depth
        }
        return requests.get(BASE_URL + "/comments/" + comment_id + "/api/morechildren/", headers=headers).json()
    # https://api.reddit.com/comments/67k25q/api/morechildren?api_type=json&showmore=true&link_id=t3_67k25q