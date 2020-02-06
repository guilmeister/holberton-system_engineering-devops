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
    name = users.json().get('name')
    todos = requests.get(url + 'todos')
    todo = todos.json()
    completed_tasks = 0
    total_tasks = 0

    for t in todo:
        if (t.get('userId') == int(sys.argv[1])):
            total_tasks = total_tasks + 1
            if (t.get('completed')):
                completed_tasks = completed_tasks + 1

    print('Employee {} is done with tasks({}/{}):'.format(name,
                                                          completed_tasks,
                                                          total_tasks))

    for t in todo:
        if (t.get('userId') == int(sys.argv[1]) and t.get('completed')):
            print('\t ' + t.get('title'))
