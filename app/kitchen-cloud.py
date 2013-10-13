#!/usr/bin/python2
#
#  Kitchen-Cloud: work in your kitchen, manage it in the cloud!
#  Copyright (C) 2013 Jonathan Pelletier.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask
from flask import url_for, request, redirect

# Mako template imports
from flask.ext.mako import MakoTemplates
from flask.ext.mako import render_template

# flask-mail imports
from flask.ext.mail import Mail, Message

# used form import
from forms.user import User

# db function import
from dbengines.dbcurrent import db

# Set to false in production
debug=True

# Application object
app = Flask(__name__)
app.template_folder = "templates"
MakoTemplates(app)

# Mail server configuration
MAIL_USERNAME = 'kitchen.cloud.dev'
app.config.update(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME=MAIL_USERNAME,
        MAIL_PASSWORD= MAIL_USERNAME+'1234',
        MAIL_DEFAULT_SENDER="noreply@kitchencloud.info"
        )

# flask-wtf configutation (for forms handling and validation)
app.config.update(
        CSRF_ENABLED = False,
        SECRET_KEY = 'SUPERSECRET'
        )

mail = Mail(app)
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=+"

# ************************ MAIN CONTROLLER HANDLERS ***************************
@app.route("/", methods=['GET','POST'])
def index():
    """ Main landing page of the kitchen-cloud application """
    # Sign up form that appears on the landing page
    user = User(request.form)

    # get method handling
    if request.method == 'GET':
        return render_template('index.html',form=user)
    # Post method with valid form
    # Im not sure but I think a lock on the database is required here
    # to prevent creation of a user between verification and this other
    # creation.
    elif request.method == 'POST' and user.validate():
        # Save the user to the database and redirect him to is profile.
        # TODO: figure out how to make a custum validator that
        # resurns false if that user already exists.
        db.user_create_signup(user.username.data,
                user.password.data,
                user.email.data)

        # Log the user in.

        # Send him to is profile.
        return redirect(url_for('profile'))

    # Post method with invalid form, display the template with it's errors
    else:
        return render_template('index.html', form=user)

@app.route("/explore")
def explore():
    """ Displays a list of features of the kitchen-cloud application """
    return render_template('404.html')

@app.route("/pricing")
def pricing():
    """ Displays the pricing plan for the application """
    return render_template('404.html')

@app.route("/login")
def login():
    """ Allow user to login into the application, provided they have
    a proper account."""
    return render_template('404.html')


@app.route("/profile")
def profile():
    """ Page that displays the pricing plan for the application """

    return render_template('profile.html')

# ***************************** HELPER METHODS ********************************
def lol():
    print "im a helper methods that LOLS"
    return

app.run(debug=debug)
