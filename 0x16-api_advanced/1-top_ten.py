#!/usr/bin/python3
""" Get top 10 hot posts """
import requests


def get_posts(response):
    """ Gets the posts """
    posts = []

    for post in response.json()['data']['children']:
        posts.append(post['data']['title'])

    return posts


def top_ten(subreddit):
    """ Returns top 10 posts """
    auth = requests.auth.HTTPBasicAuth('LqbShrCIO2ZLZQRZt7s6Fg', 'RpCwbohdiD_6h2KLPVU_y-_TJCSMZQ')
    data = {'grant_type': 'password',
            'username': 'yitbehisbro',
            'password': 'Yitbe1234%'}

    headers = {'User-Agent': 'PPP/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    params = {'limit': 10}
    title = ""

    url = "https://oauth.reddit.com/r/{}/top".format(subreddit)
    for i in range(1):
        res = requests.get(url, headers=headers, params=params)
        if res.status_code != 200:
            print("None")
            return
        posts = get_posts(res)

    for title in posts:
        print(title)
