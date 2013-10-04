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
from flask.ext.mako import MakoTemplates
from flask.ext.mako import render_template
from flask import request


# Set to false in production
debug=True

# Application object
app = Flask(__name__)
app.template_folder = "templates"
MakoTemplates(app)


@app.route("/")
def index():
    """ Main landing page of the kitchen-cloud application """
    return render_template('index.html')

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

@app.route("/signup", methods=['GET','POST'])
def signup():
    """ Page that displays the pricing plan for the application """
    return render_template('404.html')

@app.route("/profile")
def profile():
    """ Page that displays the pricing plan for the application """
    return render_template('404.html')


app.run(debug=debug)
