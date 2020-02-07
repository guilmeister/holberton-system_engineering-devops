#!/usr/bin/python3
"""Task:0 How many subs?"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit
    """
    try:
        url = 'https://www.reddit.com/r/'
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = requests.get(url + '{}/hot.json?limit=10'.format(subreddit),
                           headers=headers)
        for titles in req.json().get('data').get('children'):
            print(titles.get('data').get('title', None))
    except:
        print('None')
