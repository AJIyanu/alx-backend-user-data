# pylint: disable=relative-beyond-top-level
#!/usr/bin/env python3
"""
create expiry date for session.
"""

from os import getenv
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """create an expiry session class"""

    def __init__(self) -> None:
        """overload parent class"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """overload create session"""
        session = super().create_session(user_id)
        if session is None:
            return None
