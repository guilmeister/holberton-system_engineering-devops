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
    total_users = len(requests.get(url + 'users').json())
    new_dict = {}
    x = 1

    while (x <= total_users):
        users = requests.get(url + 'users/{}'.format(x))
        name = users.json().get('username')
        todos = requests.get(url + 'todos')
        todo = todos.json()
        new_dict[x] = []

        for t in todo:
            if t.get('userId') == x:
                new_dict.get(x).append({
                        "task": t.get('title'),
                        "completed": t.get('completed'),
                        "username": name
                        })
        x = x + 1

    with open('todo_all_employees.json', 'w') as data:
        json.dump(new_dict, data)
