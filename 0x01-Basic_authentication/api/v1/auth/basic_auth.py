#!/usr/bin/env python3
"""
Basic Authentication, child of Auth
"""
from .auth import Auth


class BasicAuth(Auth):
    """A basic authentity class"""


    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """extract base64 authorizzation header"""
        print("debug1")
        if authorization_header is None or type(authorization_header) is not str:
            return None
        print("debug2")
        if "Basic " not in authorization_header:
            return None
        else:
            return authorization_header.replace("Basic ", "")
