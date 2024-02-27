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
BASE_URL = 'https://oauth.reddit.com'

def get_hot_posts():
    return requests.get( BASE_URL + "/r/wallstreetbets/hot", headers=headers)

# ADD MORE USEFUL API HERE

