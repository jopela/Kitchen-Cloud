#!/usr/bin/env python

from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms import validators
from wtforms import ValidationError
from dbengines.dbcurrent import db
from passlib.hash import sha256_crypt

# Form used on the index view.
class Signup(Form):
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

# Form used on the login view.
class Login(Form):
    username = StringField('username')
    password = PasswordField('password')

    # custom validators.
    def validate_username(self, username):
        """ Compares the submited password to database password. """
        password = self.password.data
        dhash = db.user_hash(username.data)

        if not dhash or not sha256_crypt.verify(password, dhash):
            raise ValidationError('Username or Password invalid')
        return




