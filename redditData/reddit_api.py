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
        return requests.get(BASE_URL + "/hot?limit=100", headers=headers).json()

    # post should be in this format json.get('data').get('children')[i]
    def get_post_id(self, post):
        return post.get('data').get('id')

    # Returns a list containing the data of the post
    def get_post_data(self, id):
        return requests.get(BASE_URL + "/comments/" + id + "?limit=1000", headers=headers).json()

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

    # returns the comments, replies and individual ups, downs, and upvote ratio.
    def get_all_comments_data(self, data, res):
        for i in range(0, len(data.get('data').get('children'))):
            res = (res + f"{self.get_comment(data.get('data').get('children')[i])}"
                   + " Ups: " + f"{self.get_ups(data.get('data').get('children')[i])}"
                   + " Downs: " + f"{self.get_downs(data.get('data').get('children')[i])}"
                   + " Ratio: " + f"{self.get_upvote_ratio(data.get('data').get('children')[i])}" + "\n")
            # Access Replies
            if isinstance(data.get('data').get('children')[i].get('data').get('replies'), dict):

                res = self.get_all_comments_data(data.get('data').get('children')[i].get('data').get('replies'), res)
        return res

    # Gets the dictionaries of hidden replies and adds them to the list of dicts
    def get_more_dicts(self, comment, dicts, id, depth):
        children = ""
        children_size = len(comment.get('data').get('children'))
        for i in range(0, children_size):
            if i == children_size - 1:
                children += comment.get('data').get('children')[i]
            else:
                children += comment.get('data').get('children')[i] + ","

        # API request to get hidden replies
        replies = requests.get(BASE_URL + "/api/morechildren?link_id=t3_" + id + "&limit_children=false&depth=" + depth + "&children=" + children,headers=headers).json()
        if replies.get('jquery')[10][3][0]:
            reply_count = len(replies.get('jquery')[10][3][0])
            for i in range(0, reply_count):
                dicts.append(replies.get('jquery')[10][3][0][i].get('data'))

    # Returns a list of dictionaries
    def get_dicts(self, data, dicts, id, depth):
        size = len(data.get('data').get('children'))
        for i in range(0, size):
            # Check if the reply has any content
            if not data.get('data').get('children')[i].get('data').get('body'):
                self.get_more_dicts(data.get('data').get('children')[i], dicts, id, depth)
            else:
                dicts.append(data.get('data').get('children')[i].get('data'))
            # Get the replies to the comment
            if isinstance(data.get('data').get('children')[i].get('data').get('replies'), dict):
                self.get_dicts(data.get('data').get('children')[i].get('data').get('replies'), dicts, id, depth)

    # FUNCTIONS FOR TESTING
    # New Issue: Hidden threads under comments
    # Possible to get replies after a certain comment ID https://www.reddit.com/r/wallstreetbets/comments/1axhn74/comment/ks1vhmj/
    # Gets more replies out of comments
    def get_more_children(self, data):
        # creates a list of children ids separated by
        children = ""
        for i in range(0, len(data.get('data').get('children'))):
            if (i == len(data.get('data').get('children')) - 1):
                children += data.get('data').get('children')[i]
            else:
                children += data.get('data').get('children')[i] + ","

        # API request to get hidden replies
        replies = requests.get(BASE_URL + "/api/morechildren?link_id=t3_1axhn74&limit_children=false&depth=1000&children=" + children, headers=headers).json()
        result = ""
        if replies.get('jquery')[10][3][0]:
            for i in range(0, len(replies.get('jquery')[10][3][0])):
                if replies.get('jquery')[10][3][0][i].get('data').get('body'):
                    result = result + f"{replies.get('jquery')[10][3][0][i].get('data').get('body')}" + "\n"
                else:
                    thread = requests.get(BASE_URL + "/comments/" + id + "/comment/" + f"{replies.get('jquery')[10][3][0][i].get('data').get('id')}")
                    print(f"{replies.get('jquery')[10][3][0][i].get('data')}" + "\n")
        return result

    # Gets all comments and all replies to a comment of a post for testing
    # data should be in format post[1]
    def get_comments(self, data):
        # Prints the direct comments of the post
        size = len(data.get('data').get('children'))
        for i in range(0, size):
            # Check for none type
            if not self.get_comment(data.get('data').get('children')[i]):
                print(self.get_more_children(data.get('data').get('children')[i]))
            else:
                print(self.get_comment(data.get('data').get('children')[i]))

            # Print all replies to the comment
            if isinstance(data.get('data').get('children')[i].get('data').get('replies'), dict):
                self.get_comments(data.get('data').get('children')[i].get('data').get('replies'))