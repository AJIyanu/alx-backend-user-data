#!/usr/bin/env python3
"""crrating a basic flask app"""


from flask import Flask, jsonify, request, make_response, abort, redirect
from flask import url_for
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


@app.route("/sessions", methods=['POST', 'DELETE'], strict_slashes=False)
def sessions() -> str:
    """make a seesion id cookes"""
    if request.method == 'DELETE':
        res = request.headers.get('Cookie')
        if res is not None:
            res = res.split("session_id=")[-1]
            user = AUTH.get_user_from_session_id(res)
            if user is None:
                abort(403)
            AUTH.destroy_session(user.id)
            return redirect(url_for('payload'))
        abort(403)
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
    else:
        abort(401)
    resp = make_response(jsonify({"email": email, "message": "logged in"}))
    resp.set_cookie('session_id', session_id)
    return resp


@app.route("/termux", methods=['GET'], strict_slashes=False)
def termux_test() -> make_response:
    """for termux testing only"""
    resp = make_response(jsonify({"set cookie": "cookie"}))
    resp.set_cookie("session_id", "setting cookies")
    return resp


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile() -> str:
    """user profile getter"""
    res request.headers.get("Cookie")
    res = res.split("session_id")[-1]
    user = AUTH.get_user_from_session_id(res)
    if user is None:
        abort(403)
    return jsonify({"email": user.email})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
