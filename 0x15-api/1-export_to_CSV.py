#!/usr/bin/python3
"""
    Gather data from an API
"""
import csv
import requests
import sys

if __name__ == "__main__":
    search = sys.argv[1]
    r = requests.get(
        'https://jsonplaceholder.typicode.com/todos/',
        params={'userId': search}
    )
    r2 = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(search)
    )

    json_data = r.json()
    json_data_r2 = r2.json()
    with open("{}.csv".format(search), "w") as csvfile:
        f = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in json_data:
            f.writerow([
                task.get('userId'),
                json_data_r2.get('username'),
                task.get('completed'),
                task.get('title')
            ])
