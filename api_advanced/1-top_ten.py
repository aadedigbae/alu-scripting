#!/usr/bin/python3
"""This is recursive function that queries the Reddit
 API and returns a list containing the titles
 of all hot articles for a given subreddit"""


def top_ten(subreddit):
    """
    queries the Reddit API
    prints the titles of the first 10 hot posts for subreddit
    """
    import json
    import requests
    subreddit_URL = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
        subreddit)
    subreddit_info = requests.get(subreddit_URL,
                                  headers={"user-agent": "user"},
                                  allow_redirects=False).json()
    if "data" not in subreddit_info:
        print("None")
        return
    children = subreddit_info.get("data").get("children")
    for child in children:
        print(child.get("data").get("title"))
