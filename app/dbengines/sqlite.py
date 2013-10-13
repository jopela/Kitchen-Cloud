#!/usr/bin/env python
# The sqlite3 backend implementation of the database function.
from contextlib import contextmanager
from passlib.hash import sha256_crypt
import sqlite3


# TODO: specify the database connection details in a config file or
# get it from the command line argument. For the moment, just hardcode in
# the app.
con_str ='../../db/kcdb'

def test():
    """ used for testing ... NEEDS TO BE REPLACED BY SERIOUS TESTING """

    # since this is a test, override the value of con_str.
    result = user_uname_exists("jopela")
    print result, type(result)
    return

def user_uname_exists(uname):
    """ Returns True if this username exists in the database user table. False
    otherwise. """
    return field_exists('user', 'username', uname)

def user_email_exists(email):
    """ Returns True if this email exists in the database user table. False
    otherwise. """
    return field_exists('person', 'email', email)

# TODO: should we raise an exception if this fails for some reason?
# how should we treat errors? For the moment assume the world is a perfect,
# errorless place.
def user_create_signup(username, password, email):
    """ Create a new user in the database when someone signs up for the
    application. """

    # Create a person in the database.
    person_create(email)

    # Get the newly create id so we can tie it with the user.
    person_id = person_id_email(email)

    # Hash the user password.
    dbhash = sha256_crypt.encrypt(password)

    # Store everything in the db. Note that the status == 1 means ACTIVE.
    user_create(username, dbhash, person_id, 1)
    return

def user_create(username, hash, person, status):
    """ Create a user in the database. """
    param = (username, hash, person, status)
    sql = "insert into user (username, hash, person, status) values (?,?,?,?)"

    with sqlite3.connect(con_str) as con:
        con.execute(sql,param)
    return

def person_create(email, firstname=None,lastname=None):
    """ Create a new person in the database. """
    param = (firstname, lastname, email)
    sql = "insert into person (firstname, lastname, email) values (?,?,?)"
    with sqlite3.connect(con_str) as con:
        # insert the person.
        con.execute(sql, param)
    return

def person_id_email(email):
    """ Return a person id given it's email. """
    param = (email,)
    sql = "select id from person where email=?"
    with sqlite3.connect(con_str) as con:
        person_id = con.cursor().execute(sql,param).fetchone()[0]
    return person_id

##########################
# database helper methods.
##########################
def field_exists(tname, fname, value):
    """ Returns True if value of fname exists in the table tname. False
    otherwise. """
    param = (value,)
    # sql injections arent a problem here because tname and fname are not
    # provided as user input but by the application. A case could surely be
    # made that this is still insecure but let's ignore it at this point.
    sql = "SELECT count(*) from {0} where {1}=?".format(tname, fname)
    with sqlite3.connect(con_str) as con:
        result = con.cursor().execute(sql, param).fetchone()[0] == 1
    return result

if __name__ == '__main__':
    test()




