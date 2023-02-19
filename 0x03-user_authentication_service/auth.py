#!/usr/bin/env python3
"""
Hashes a password
"""


from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """You alakobian. I will commemt"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registers a user to database"""
        db = self._db
        try:
            check = db.find_user_by(email=email)
            raise ValueError("User <user's email> already exists")
        except NoResultFound:
            password = _hash_password(password)
            return db.add_user(email, password)


def _hash_password(password: str) -> bytes:
    """returns a byted hashed password"""
    import bcrypt

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
