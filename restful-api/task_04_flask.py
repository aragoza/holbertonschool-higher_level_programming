#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/status")
def go_get_status_code():
    """
    Docstring for go_get_status_code
    """
    return "OK", 200

@app.route("/")
def home():
    """
    Docstring for home
    """
    return "Welcome to the Flask API!", 200

@app.route("/data", methods=["GET"])
def go_get_data():
    """
    Docstring for get_data
    """
    data_username = list(users.keys())
    return jsonify(data_username), 200

@app.route("/data/<string:username>", methods=["GET"])
def go_go_go_data(username):
    """
    Docstring for go_go_go_data
    """
    return jsonify(users[username])



if __name__ == "__main__":
    app.run()
