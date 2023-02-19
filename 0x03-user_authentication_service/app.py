#!/usr/bin/env python3
"""crrating a basic flask app"""


from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=["GET"], strict_slashes=False)
def payload() -> str:
    """return payload jsonify"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def users() -> str:
    """registers users"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is not None and password is not None:
        try:
            user = AUTH.register_user(email, password)
            return jsonify({"email": user.email, "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
