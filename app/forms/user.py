#!/usr/bin/env python

from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms import validators

class User(Form):
    username = StringField('Your username', [validators.Length(min=4)])
    password = PasswordField('Your password', [validators.Length(min=8)])
    email = StringField('Your email', [validators.Email()])



