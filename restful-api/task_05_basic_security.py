#!/usr/bin/env python3
"""
Docstring for holbertonschool-higher_level_programming.restful-api.task_05_basic_security
"""


from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": {
        "password": generate_password_hash("admin123"),
        "role": "admin"
    },
    "user": {
        "password": generate_password_hash("user123"),
        "role": "user"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Docstring for verify_password

    :param username: Description
    :param password: Description
    :return: Description
    :rtype: Any | None
    """
    if username in users and check_password_hash(users[username]["password"], password):
        return username

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    Docstring for basic_protected

    :return: Description
    :rtype: tuple[Response, Literal[200]]
    """
    return jsonify("Hello {} (Basic Auth)".format(auth.current_user())), 200

@app.route("/login", methods=["POST"])
def login():
    """
    Docstring for login

    :return: Description
    :rtype: tuple[Response, Literal[200]] | Literal[401]
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token), 200

    return 401

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Docstring for jwt_protected

    :return: Description
    :rtype: tuple[Response, Literal[200]] | Literal[401]
    """
    if not get_jwt_identity():
        return 401
    return jsonify("JWT Auth: Access Granted"), 200

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Docstring for admin_only

    :return: Description
    :rtype: tuple[Response, Literal[403]] | tuple[Response, Literal[200]]
    """
    current_user = get_jwt_identity()
    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify("Admin Access: Granted"), 200

if __name__ == '__main__':
    app.run()
