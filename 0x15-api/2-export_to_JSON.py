#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID, returns information
about his/her TODO list progress.
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users/{}'.format(sys.argv[1]))
    name = users.json().get('username')
    todos = requests.get(url + 'todos')
    todo = todos.json()
    new_dict = {sys.argv[1]: []}

    for t in todo:
        if t.get('userId') == int(sys.argv[1]):
            new_dict.get(sys.argv[1]).append({
                "task": t.get('title'),
                "completed": t.get('completed'),
                "username": name
                })

    with open('{}.json'.format(sys.argv[1]), 'w') as data:
        json.dump(new_dict, data)
