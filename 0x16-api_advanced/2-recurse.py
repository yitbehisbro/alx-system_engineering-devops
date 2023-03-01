#!/usr/bin/python3
""" Get top all hot posts """
import requests


def recurse(subreddit, hot_list=[]):
    """ Returns top posts """
    headers = {'User-Agent': 'PPP/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200 or res.status_code == 301:
        return None

    js = res.json()
    posts = js.get('data').get('children')
    if not posts:
        return None
    hot_list.append(posts[len(hot_list)].get('data').get('title'))
    if len(hot_list) == 0:
        return "OK"
    if len(hot_list) < len(posts):
        recurse(subreddit)
    return hot_list
