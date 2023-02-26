#!/usr/bin/env python3
"""It’s the first step for creating
a new authentication mechanism"""


from .auth import Auth


class SessionAuth(Auth):
    """
    validate if everything inherits correctly without any overloading
    validate the “switch” by using environment variables
    """
    pass
