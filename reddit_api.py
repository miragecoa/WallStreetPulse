import requests
# Setting up authorization header
ID = "mGJKXOitGGulU5pBJ9Zmqg"
SECRIT_KEY = "zZR3V_O4kRdzjJqKZN9-oNluADiHfg"
auth = requests.auth.HTTPBasicAuth(ID, SECRIT_KEY)

with open('pswd.txt', 'r') as f:
    pswd = f.read()

# https://www.reddit.com/prefs/apps
# https://old.reddit.com/prefs/apps/
data = {
    'grant_type': 'password',
    'username': 'WallStreetPulse',
    'password' : pswd
}

headers = {'User-Agent': "WallStreetPulse/0.0.1"}
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'


# Request using API
# API can be found https://www.reddit.com/dev/api/
BASE_URL = 'https://oauth.reddit.com/r/wallstreetbets'

def get_hot_posts():
    return requests.get( BASE_URL + "/hot", headers=headers)

# ADD MORE USEFUL API HERE
# Returns a list containing the data of the post
def get_post_data(id):
    return requests.get ( BASE_URL + "/comments/" + id, headers=headers)

def get_post_content(comments_list):
    print(comments_list[0].get('data').get('children')[0].get('data').get('selftext'))
def get_comments(comments_list):
    # Prints the direct comments of the post
    for i in range(0, len(comments_list.get('data').get('children'))):
        print(comments_list.get('data').get('children')[i].get('data').get('body'))
        # Print the replies to the comment
        if isinstance(comments_list.get('data').get('children')[i].get('data').get('replies'), dict):
            get_comments(comments_list.get('data').get('children')[i].get('data').get('replies'))
