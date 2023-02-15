#!/usr/bin/env python3
"""
This is authentication module longer long
"""


class Auth:
    """Authenticate me please
    how long do I  need"""
    from flask import Request
    from typing import List, TypeVar

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """requires authenticatiion here, returns False """
        if excluded_paths is None:
            return True
        if path in excluded_paths:
            return False
        if "/api/v1/status/" in excluded_paths and path == "/api/v1/status":
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """does nothing yet, returns none"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """does nothing too, returns none"""
        return None
