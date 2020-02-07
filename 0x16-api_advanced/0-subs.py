#!/usr/bin/python3
"""Task:0 How many subs?"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit
    """
    url = 'https://www.reddit.com/r/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = requests.get(url + '{}/about.json'.format(subreddit),
                       headers=headers)
    if req:
        return req.json().get('data').get('subscribers')
    else:
        return 0
