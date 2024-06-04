#!/usr/bin/python3
"""
A script that contains a method to return the number of subs
crilelers to a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subredditk
    .Returns
    the number of subscribers for a given subreddit"""
    headers = {"User-Agent": "xica369"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
