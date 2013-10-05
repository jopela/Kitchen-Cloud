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

# model import
from models import user

# used form import
from forms.user import User

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
        MAIL_PASSWORD= MAIL_USERNAME+'1234'
        )

# flask-wtf configutation (for forms handling and validation)
app.config.update(
        CSRF_ENABLED = True,
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

    if request.method == 'GET':
        return render_template('index.html',form=user)

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
    return render_template('404.html')

# ***************************** HELPER METHODS ********************************
def lol():
    print "im a helper methods that LOLS"
    return

app.run(debug=debug)
