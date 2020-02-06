#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users/{}'.format(sys.argv[1]))
    name = users.json().get('username')
    todos = requests.get(url + 'todos')
    todo = todos.json()
    completed_tasks = 0
    total_tasks = 0

    with open('{}.csv'.format(sys.argv[1]), 'w') as data:
        for t in todo:
            if (t.get('userId') == int(sys.argv[1])):
                data.write('"{}","{}","{}","{}"\n'.format(t.get('userId'),
                                                          name,
                                                          t.get('completed'),
                                                          t.get('title')))
