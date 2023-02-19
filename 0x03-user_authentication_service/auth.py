#!/usr/bin/env python3
"""
Hashes a password
"""

def _hash_password(password: str) -> bytes:
    """returns a byted hashed password"""
    import bcrypt

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)
