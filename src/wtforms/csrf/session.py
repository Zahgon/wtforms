"""
A provided CSRF implementation which puts CSRF data in a session.

This can be used fairly comfortably with many `request.session` type
objects, including the Werkzeug/Flask session store, Django sessions, and
potentially other similar objects which use a dict-like API for storing
session keys.

The basic concept is a randomly generated value is stored in the user's
session, and an hmac-sha1 of it (along with an optional expiration time,
for extra security) is used as the value of the csrf_token. If this token
validates with the hmac of the random value + expiration time, and the
expiration time is not passed, the CSRF validation will pass.
"""

import hmac
import os
from datetime import datetime
from datetime import timedelta
from hashlib import sha1

from ..validators import ValidationError
from .core import CSRF

__all__ = ("SessionCSRF",)


class SessionCSRF(CSRF):
    TIME_FORMAT = "%Y%m%d%H%M%S"




    def now(self):
        """
        Get the current time. Used for test mocking/overriding mainly.
        """
        pass


