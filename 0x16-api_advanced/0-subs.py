import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "my_reddit_app/0.1 by u/your_username"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["data"]["subscribers"]
    except requests.exceptions.HTTPError:
        return 0