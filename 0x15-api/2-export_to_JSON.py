#!/usr/bin/python3
""" export data in the JSON format """
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/"
    request = requests.get(url)
    line = "{\"" + sys.argv[1] + "\": ["

    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    req = requests.get(url)
    user = req.json()
    user = user.get('username')

    for value in request.json():
        if int(value.get('userId')) == int(sys.argv[1]):
            s = str(value.get('completed')).lower()
            t = value.get('title')
            c = "completed"
            ts = "task"
            u = "username"
            b = "{\""
            e = "\"}, "
            k = "\": "
            a = "\": \""
            ss = ", \""
            sep = "\", \""

            line += b + ts + a + t + sep + c + k + s + ss + u + a + user + e
    line = line.rstrip(', /.')
    line = line + "]}"
    filename = sys.argv[1] + ".json"
    with open(filename, mode='w', encoding="utf-8") as files:
        files.write(line)
