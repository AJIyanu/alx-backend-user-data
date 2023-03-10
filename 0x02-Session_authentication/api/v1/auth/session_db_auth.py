#!/usr/bin/env python3
"""session auth database"""

from models.user_session import UserSession
from .session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta

class SessionDBAuth(SessionExpAuth):
    """session suth db"""

    def create_session(self, user_id=None) -> str:
        """creates session for user id"""
        user_sess = UserSession(user_id=user_id)
        user_sess.save()
        sess_dict = {"user_id": user_id,
                     "created_at": datetime.now()
                     }
        session = user_sess.session_id
        self.user_id_by_session_id.update({session: sess_dict})
        return user_sess.session_id

    def user_id_for_session_id(self, session_id=None) -> str:
        """overload user id for session"""
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        if self.session_duration <= 0:
            sess_dict = self.user_id_by_session_id.get(session_id)
            return sess_dict.get("user_id")
        created = self.user_id_by_session_id.get(session_id)
        created = created.get("created_at")
        if created is None:
            return None
        current = created + timedelta(seconds=self.session_duration)
        if datetime.now() > current:
            return None
        user = UserSession.search({"session_id": session_id})
        return user[0].user_id if len(user) > 0 else None 

    def destroy_session(self, request=None) -> bool:
        """destroy session based on cookie"""
        if request is None:
            return False
        sess_id = self.session_cookie(request)
        if sess_id is None:
            return False
        user = UserSession.search({"session_id": sess_id})
        user[0].remove()
        return True
