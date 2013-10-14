#!/usr/bin/env python
# This file alone needs to be changed when switching backend.

import sqlite
import postgresql
import mariadb
from flask.ext.login import UserMixin


# To switch backend assign the db variable to some other import from the list
# above.
db = sqlite

# User class needed by flask-login.
class User(UserMixin):

    def __init__(self, userid):
        self.user = db.user(userid)
    def is_active(self):
        return self.user[4] == 1

    def get_id(self):
        return self.user[0]

    def is_authenticated(self):
        result = db.field_exists("authenticated", "id", self.get_id())
        return result

