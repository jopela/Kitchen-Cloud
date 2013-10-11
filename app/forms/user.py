#!/usr/bin/env python

from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms import validators
from wtforms import ValidationError
# Seriously, I do not understand why this work.
from models import user

# messing with the python path ...
import sys

user.create_user()

# labels for form classes must be the same as the templates label since they
# are used by some function to populate the for tag of some elements in forms.

class User(Form):
    username = StringField('username', [validators.Length(min=4)])
    password = PasswordField('password', [validators.Length(min=8)])
    email = StringField('email', [validators.Email()])

    # custom validators.

    def validate_username(self, username):
        print "tryring to validate"
        return



