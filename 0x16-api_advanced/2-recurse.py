#!/usr/bin/python3
""" Get top all hot posts """
import requests


def recurse(subreddit, hot_list=[]):
    """ Returns top posts """
    client = 'LqbShrCIO2ZLZQRZt7s6Fg'
    secret = 'RpCwbohdiD_6h2KLPVU_y-_TJCSMZQ'
    url = 'https://www.reddit.com/api/v1/access_token'
    auth = requests.auth.HTTPBasicAuth(client, secret)
    data = {'grant_type': 'password',
            'username': 'yitbehisbro',
            'password': 'Yitbe1234%'}

    headers = {'User-Agent': 'PPP/0.0.1'}
    res = requests.post(url, auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    url = "https://oauth.reddit.com/r/{}/top".format(subreddit)
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return None

    js = res.json()
    posts = js.get('data').get('children')
    # print(posts[len(hot_list)].get('data').get('title'))
    # print("{} of {}".format(len(hot_list), len(posts)))
    hot_list.append(posts[len(hot_list)].get('data').get('title'))
    if len(hot_list) < len(posts):
        recurse(subreddit)
    return hot_list
