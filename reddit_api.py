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
# title of the post
# comments
# upvote count ups
# downvote count downs
# upvote ratio upvote_ratio
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

    # Returns a list containing the data of the post
    def get_post_data(self, id):
        return requests.get(BASE_URL + "/comments/" + id, headers=headers).json()

    # Returns the content in the post
    def get_post_content(self, comments_list):
        print(comments_list[0].get('data').get('children')[0].get('data').get('selftext'))

    # Gets all comments and all replies to a comment
    def get_comments(self, comments_list):
        # Prints the direct comments of the post
        for i in range(0, len(comments_list.get('data').get('children'))):
            print(comments_list.get('data').get('children')[i].get('data').get('body'))
            # dict_keys(['count', 'name', 'id', 'parent_id', 'depth', 'children'])
            print(comments_list.get('data').get('children')[i].get('data').get('depth'))
            print(comments_list.get('data').get('children')[i].get('data').get('children'))

            # Print all replies to the comment
            if isinstance(comments_list.get('data').get('children')[i].get('data').get('replies'), dict):
                self.get_comments(comments_list.get('data').get('children')[i].get('data').get('replies'))

    # Gets a comment and all its replies
    # comment should be in format post[1].get('data').get('children')[num]
    def get_comment(self, comment):
        # Prints the direct comment of the post
        print(comment.get('data').get('body'))

        # Print the replies to the comment
        if isinstance(comment.get('data').get('replies'), dict):
            self.get_comments(comment.get('data').get('replies'))
