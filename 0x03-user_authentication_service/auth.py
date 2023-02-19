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

    def valid_login(self, email: str, password: str) -> bool:
        """checks if passwodd is falid"""
        import bcrypt
        db = self._db
        try:
            user = db.find_user_by(email=email)
            hsh_pwd = _hash_password(password)
            if bcrypt.checkpw(user.hashed_password, hsh_pwd):
                return True
        except NoResultFound:
            return False
        return False


def _hash_password(password: str) -> bytes:
    """returns a byted hashed password"""
    import bcrypt

    salt = "rSHyS1at74eSeJ71"
    salt = salt.encode('utf-8')
    return bcrypt.hashpw(password.encode('utf-8'), salt)
