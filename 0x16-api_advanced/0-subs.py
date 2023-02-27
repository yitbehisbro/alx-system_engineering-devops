#!/usr/bin/python3
""" Prints the subscribers to subreddit """

import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    headers = {'User-Agent': 'PPP/0.0.1'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers=headers)
    if req.status_code != 200:
        return 0
    js = req.json()

    return js.get('data').get('subscribers')
