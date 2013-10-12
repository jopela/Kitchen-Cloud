#!/usr/bin/env python

from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms import validators
from wtforms import ValidationError
# Seriously, I do not understand why this work.
from dbengines import sqlite as db

# labels for form classes must be the same as the templates label since they
# are used by some function to populate the for tag of some elements in forms.

class User(Form):
    username = StringField('username', [validators.Length(min=4)])
    password = PasswordField('password', [validators.Length(min=8)])
    email = StringField('email', [validators.Email()])

    # custom validators.
    def validate_username(self, username):
        """ Make certain that the username is not in the database."""
        if db.user_uname_exists(username.data):
            raise ValidationError('User already exists')
        return

    def validate_email(self, email):
        """ Make certain the email address in not already in the dabatase ."""
        if db.user_email_exists(email.data):
            raise ValidationError('Email already exists')
        return



