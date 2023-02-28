#!/usr/bin/python3
""" Get top 10 hot posts """
import requests


def get_posts(response):
    """ Gets the posts """
    posts = []

    for post in response.json().get('data').get('children'):
        posts.append(post.get('data').get('title'))

    return posts


def top_ten(subreddit):
    """ Returns top 10 posts """
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
    params = {'limit': 10}
    title = ""

    url = "https://oauth.reddit.com/r/{}/top/?t=now".format(subreddit)
    for i in range(1):
        res = requests.get(url, headers=headers, params=params)
        if res.status_code != 200 or res.status_code == 301:
            print("None")
            return
        posts = get_posts(res)

    for title in posts:
        print(title)
