
# https://developers.google.com/custom-search/v1/overview
# search engine id: b3dc3b1ce374e440c
# api key: AIzaSyBG2uCYJDwpZLlVcsmracUk3zRSJZMpn98
import requests
from datetime import datetime

# Define the base URL for the Custom Search JSON API
base_url = "https://www.googleapis.com/customsearch/v1"

# params
#   start_date: string with format %Y%m%d
#   end_date: string with format %Y%m%d
# returns
# a list of all article id during the given time period
def search_by_time_period(start_date = "20231203", end_date = "20240110"):
    article_ids = []
    num = 10
    while(int(start_date) < int(end_date) and num == 10):
        print(f'Request from Google: {start_date} {end_date}')
        params = {
            "key": "AIzaSyBG2uCYJDwpZLlVcsmracUk3zRSJZMpn98", # The API key
            "cx": "b3dc3b1ce374e440c", # The CSE ID
            "q": "reddit", # The search query
            "sort": f"date:r:{start_date}:{end_date}", # The date range filter
            "num": 10 # The number of results to return
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            num = len(data["items"])
            for item in data["items"]:
                article_ids.append(item['link'].split('/')[-3])
                date_obj = datetime.strptime(item['snippet'][:12].lstrip().rstrip(), "%b %d, %Y")
                start_date = max(date_obj.strftime("%Y%m%d"),start_date)
        else:
            print(f"Request failed with status code {response.status_code}")
    print("Finished all requests")
    return article_ids

if __name__ == "__main__":
    search_by_time_period()