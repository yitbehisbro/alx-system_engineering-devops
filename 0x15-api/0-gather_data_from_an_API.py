#!/usr/bin/python3
""" Fetches the data from website """
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/"
    request = requests.get(url)
    counter = done = 0
    emp = tasks = ""

    for value in request.json():
        if int(value.get('userId')) == int(sys.argv[1]):
            counter += 1
            if str(value.get('completed')) == "True":
                done += 1
                tasks += "\t " + value.get('title') + "\n"

    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    request = requests.get(url)
    value = request.json()
    emp = value.get('name')
    print("Employee {} is done with tasks({}/{}):".format(emp, done, counter))
    print("{}".format(tasks), end="")
