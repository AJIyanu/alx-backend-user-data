#!/usr/bin/env python3
"""crrating a basic flask app"""


from flask import Flask, jsonify, request, make_response, abort, Response
from flask import redirect
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
    """Response.setCookie("session_id", session_id)"""
    resp = make_response('nothing, absolutely nothing')
    resp.set_cookie('session_id', str(session_id))
    return jsonify({"email": email, "message": "logged in"})


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """Find the user with the requested session ID.
    If the user exists destroy the session and redirect
    the user to GET /. If the user does not exist, respond
    with a 403 HTTP status."""
    session_id = request.cookies.get("session_id")
    if session_id is not None:
        AUTH.destroy_session(session_id)
        return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
