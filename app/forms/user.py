#!/usr/bin/env python

from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms import validators

# labels for form classes must be the same as the templates label since they
# are used by some function to populate the for tag of some elements in forms.

class User(Form):
    username = StringField('username', [validators.Length(min=4)])
    password = PasswordField('password', [validators.Length(min=8)])
    email = StringField('email', [validators.Email()])



