#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    """
    Docstring for home
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def go_get_data():
    """
    Docstring for get_data

    :param username: Description
    """
    data_username = [user["username"] for user in users]
    return jsonify(data_username)
    

if __name__ == "__main__":
    app.run()