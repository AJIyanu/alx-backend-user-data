#!/usr/bin/env python3
"""session auth database"""

from .session_exp_auth.py import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """session suth db"""

    def create_session(self, user_id=None):
        """creates session for user id"""

