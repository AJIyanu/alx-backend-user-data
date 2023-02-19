#!/usr/bin/env python3
"""crrating a basic flask app"""


from flask import Flask, jsonify, request, make_response, abort
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


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def sessions() -> str:
    """make a seesiom id cookes"""
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
    else:
        abort(401)
    resp = make_response('nothing, absolutely nothing')
    resp.set_cookie('session_id', str(ession_id))
    return jsonify({"email": email, "message": "logged in"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
