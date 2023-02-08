#!/usr/bin/python3
""" export data in the CSV format """
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/"
    request = requests.get(url)
    line = ""

    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    req = requests.get(url)
    user = req.json()
    user = user.get('username')

    for value in request.json():
        if int(value.get('userId')) == int(sys.argv[1]):
            s = value.get('completed')
            t = value.get('title')
            i = sys.argv[1]
            sep = "\",\""

            line += "\"" + i + sep + user + sep + str(s) + sep + t + "\"\n"

    filename = sys.argv[1] + ".csv"
    with open(filename, mode='w', encoding="utf-8") as files:
        files.write(line)
