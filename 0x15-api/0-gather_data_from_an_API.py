#!/usr/bin/python3
""" Python script that uses REST API to fetch.
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    user = get('https://jsonplaceholder.typicode.com/users/' + argv[1])
    name = user.json().get("name")
    todo = get('https://jsonplaceholder.typicode.com/todos')
    todos = todo.json()
    task_list = []
    tasks = 0
    completed = 0
    for item in todos:
        if item.get("userId") == int(argv[1]):
            tasks += 1
            if item.get("completed") is True:
                completed += 1
                task_list.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format
          (name, completed, tasks))

    for i in task_list:
        print("\t {}".format(i))
