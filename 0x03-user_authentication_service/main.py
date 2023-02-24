#!/usr/bin/env python3
"""unitest for basic authentification"""

import requests


url = "http://0.0.0.0:5000"

def register_user(email: str, password: str) -> None:
    """checks register user"""
    params = {"email": email, "password": password}
    res = requests.post(url + "/users", params=params)
    assert res.status_code == 200
    res = requests.post(url + "/users", params=params)
    assert res.status_code == 400


def log_in_wrong_password(email: str, password: str) -> None:
    """test wrong password"""
    params = {"email": email, "password": password}
    res = requests.post(url + "/sessions", params=params)
    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """log in with real password"""
    params = {"email": email, "password": password}
    res = requests.post(url + "/sessions", params=params)
    session_id = res.cookies.get("session_id")
    assert res.status_code == 200
    return session_id


def profile_unlogged() -> None:
    """log me out"""



def profile_logged(session_id: str) -> None:
    """profile logged in"""
    res = requests.get(url + "/profile")
    assert res.status_code == 200


def log_out(session_id: str) -> None:
    res = requests.delete(url + "/sessions")
    assert res.status_code == 403


def reset_password_token(email: str) -> str:
    """resets email password"""
    res = requests.post(url + "/reset_password", params={"email": email})
    print(res.content)
    print(type(res.content))
    assert res.status_code == 200


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """updates password with token"""
    params = {"email": email, "reset_token": reset_token, "new_password": new_password}
    res = requests.put(url + "reset_password", params=params)
    assert res.status_code == 200

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
