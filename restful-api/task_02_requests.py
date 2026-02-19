#!/usr/bin/python3
"""
Docstring for restful-api.task_02_requests
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Docstring for fetch_and_print_posts
    """
    URL = "https://jsonplaceholder.typicode.com/posts"

    responce = requests.get(URL)
    print(f"Status Code: {responce.status_code}")

    if responce.status_code != 200:
        return()
    else:
        data = responce.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    """
    Docstring for fetch_and_save_posts
    """
    URL = "https://jsonplaceholder.typicode.com/posts"

    responce = requests.get(URL)

    if responce.status_code != 200:
        return()
    else:
        data = responce.json()

        data = [
            [post["id"], post["title"], post["body"]]
            for post in data
        ]

    with open("posts.csv", "w", newline="", encoding="utf-8") as csv_file:
        csv_write = csv.writer(csv_file)

        csv_write.writerow(["id", "title", "body"])

        for line in data:
            csv_write.writerow(line)

fetch_and_print_posts()
fetch_and_save_posts()