#!/usr/bin/env python3
"""It’s the first step for creating
a new authentication mechanism"""


import sys
import os
parent_dir = os.path.abspath(os.path.join('models'))
sys.path.insert(0, parent_dir)


import uuid
from .auth import Auth
from models.user import User


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
        uid = str(uuid.uuid4())
        self.user_id_by_session_id.update({uid: user_id})
        return uid

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns user based on cookies"""
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        return User.get(user_id)
