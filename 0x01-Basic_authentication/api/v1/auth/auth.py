#!/usr/bin/env python3
"""
This is authentication module longer long
"""


from flask import Request
from typing import List, TypeVar


class Auth:
    """Authenticate me please
    how long do I  need"""


    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """requires authenticatiion here, returns False """
        return False

    def authorization_header(self, request=None) -> str:
        """does nothing yet, returns none"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """does nothing too, returns none"""
        return None
