#!/usr/bin/python3
"""
Docstring
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Docstring
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print("Status Code: ".format(r.status_code))

    if r.status_code != 200:
        return
    else:
        temp = r.json()
        for i in temp:
            print("{}".format(i['title']))


def fetch_and_save_posts():
    """
    Docstring
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    if r.status_code != 200:
        return
    else:
        data = r.json()

        listing =[]
        for post in data:
            listing.append([
                post["id"], post["title"], post["body"]
            ])

    with open("posts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["id", "title", "body"])

        for line in listing:
            writer.writerow(line)

fetch_and_print_posts()
fetch_and_save_posts()
