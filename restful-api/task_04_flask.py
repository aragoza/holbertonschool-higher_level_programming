#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)


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

@app.route("/users/<string:username>", methods=["GET"])
def go_go_go_data(username):
    """
    Docstring for go_go_go_data
    """
    if username not in users:
        return {"error": "User not found"}, 404
    return jsonify(users[username]), 200

@app.route("/add_user", methods=["POST"])
def post_a_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in data or not data["username"]:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run()
