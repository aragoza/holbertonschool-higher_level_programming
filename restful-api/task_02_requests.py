#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print(r.status_code)

    if r.status_code != 200:
        return
    else:
        temp = r.json()
        for i in temp:
            print("{}".format(i['title']))


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    if r.status_code != 200:
        return
    else:
        data = r.json()

        posts_list = []
        for post in data:
            posts_list.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(posts_list)
