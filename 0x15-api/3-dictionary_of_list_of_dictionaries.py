#!/usr/bin/python3
""" a Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress."""
import json
import requests
import sys


if __name__ == '__main__':
    data = {}
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    r2 = requests.get(url2)
    for item in r2.json():
        if item.get('userId') not in data:
            data[item.get('userId')] = []
        url = 'https://jsonplaceholder.typicode.com/users/'\
              + str(item.get('userId'))
        username = requests.get(url).json().get('username')
        d = {'task': item.get('title'),
             'completed': item.get('completed'),
             'username': username}
        data[item.get('userId')].append(d)

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as f:
        json.dump(data, f)
