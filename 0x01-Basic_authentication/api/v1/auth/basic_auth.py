#!/usr/bin/env python3
"""
Basic Authentication, child of Auth
"""
from .auth import Auth


class BasicAuth(Auth):
    """A basic authentity class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract base64 authorizzation header"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if "Basic " not in authorization_header:
            return None
        else:
            return authorization_header.replace("Basic ", "")

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """decode base 64"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        import base64
        try:
            return base64.b64decode(
                    base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """returns tuple of username and email"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        split = decoded_base64_authorization_header.split(":")
        return (split[0], split[1])
