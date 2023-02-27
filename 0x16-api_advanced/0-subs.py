#!/usr/bin/python3
""" Prints the subscribers to subreddit """

import requests
import sys


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(sys.argv[1])
    req = requests.get(url)
    js = req.json()
    return js.get('data').get('subscribers')
