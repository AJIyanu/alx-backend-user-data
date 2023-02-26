#!/usr/bin/env python3
"""It’s the first step for creating
a new authentication mechanism"""


import uuid
from .auth import Auth


class SessionAuth(Auth):
    """
    validate if everything inherits correctly without any overloading
    validate the “switch” by using environment variables
    """
    user_id_by_session_id = {}


    def create_session(self, user_id: str = None) -> str:
        """that creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        uid = uuid.uuid4()
        self.user_id_by_session_id.update({uid: user_id})
        return uid
