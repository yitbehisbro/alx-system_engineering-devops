#!/usr/bin/python3
""" Get top 10 hot posts """
import requests


def top_ten(subreddit):
    """ Returns top 10 posts """
    headers = {'User-Agent': 'PPP/0.0.1'}
    params = {'limit': 10}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    posts = []

    for i in range(1):
        res = requests.get(url, headers=headers, params=params,
                           allow_redirects=False)
        if res.status_code != 200 or res.status_code == 301:
            print("None")
            return
        for post in res.json().get('data').get('children'):
            posts.append(post.get('data').get('title'))

    for title in posts:
        print(title)
