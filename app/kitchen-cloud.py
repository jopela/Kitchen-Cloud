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

from passlib.hash import sha256_crypt

from flask import Flask
from flask import url_for, request, redirect

# Mako template imports
from flask.ext.mako import MakoTemplates
from flask.ext.mako import render_template

# flask-mail imports
from flask.ext.mail import Mail, Message

# flask-login imports
from flask.ext.login import LoginManager
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.ext.login import current_user
from flask.ext.login import logout_user

# user form import
from forms.user import Signup
from forms.user import Login

# db function import
from dbengines.dbcurrent import db
from dbengines import dbcurrent

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

mail = Mail(app)

# flask-wtf configutation (for forms handling and validation)
app.config.update(
        CSRF_ENABLED = False,
        SECRET_KEY = 'as@f^2D9jjd2$cAd8*/-a5^fa!sabn0!240xC^3)-'
        )

# flask-login configuration (for user session purpuses)
login_manager = LoginManager(app)

# if user arent logged in and request a page that requires so, they are sent
# to this view.
login_manager.login_view = "login"

# the user_loader callback required by flask-login
@login_manager.user_loader
def load_user(userid):
    return dbcurrent.User(userid)

# ************************ MAIN CONTROLLER HANDLERS ***************************
@app.route("/", methods=['GET','POST'])
def index():
    """ Main landing page of the kitchen-cloud application """
    # Sign up form that appears on the landing page
    user = Signup(request.form)

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

        # Authenticate and log the user in.
        auth_and_login(user.username.data)

        # Send him to is profile now.
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

@app.route("/login", methods=['GET','POST'])
def login():
    """ Allow user to login into the application, provided they have
    a proper account."""

    user = Login(request.form)

    if request.method == 'POST' and user.validate():
        # Authenticate, log and redirect them.
        auth_and_login(user.username.data)
        return redirect(url_for('profile'))
    else:
        # GET request or POST with errors.
        return render_template('login.html', form=user)

@app.route("/profile")
@login_required
def profile():
    """ Page where the user lands once login is completed. """
    return render_template('profile.html', user=current_user)

@app.route("/logout")
@login_required
def logout():
    """ Function to logout the user and redirect him to the index page. """
    username = current_user.user[1]
    deauth_and_logout(username)

    return redirect(url_for('index'))


# ***************************** HELPER METHODS ********************************
def auth_and_login(username):
    """ Authenticate a user in the database and log him in. """
    db.authenticate(username)
    uid = db.user_id(username)
    login_user(dbcurrent.User(uid))
    return

def deauth_and_logout(username):
    """ De-authenticate a user in the database and log him out. """
    db.deauthenticate(username)
    logout_user()
    return

app.run(debug=debug)
