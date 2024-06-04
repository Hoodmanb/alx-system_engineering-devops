#!/usr/bin/python3
"""
A script that has a method that prints
the titles of the first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    A method that prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "custom_user_agent_v1.0"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)

    if response.status_code == 200:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title', None))
    else:
        print(None)


# Example usage
# top_ten("python")
