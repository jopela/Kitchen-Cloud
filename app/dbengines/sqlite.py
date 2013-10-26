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
    pid = person_id(email)

    # Hash the user password.
    dbhash = sha256_crypt.encrypt(password)

    # Store everything in the db. Note that the status == 1 means ACTIVE.
    user_create(username, dbhash, pid, 1)
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

def person_id(email):
    """ Return a person id given it's email. """
    param = (email,)
    sql = "select id from person where email=?"
    with sqlite3.connect(con_str) as con:
        pid = con.cursor().execute(sql,param).fetchone()
        pid = pid[0] if pid else None
    return pid

def user_id(username):
    """ Return a user id given it's username. """
    return from_field("user", "id", "username", username)[0][0]

def user(userid):
    """ Return a user from the database given it's id stored there. """
    return from_id("user",userid)

def user_hash(username):
    """ Return the user hash from it's username . """
    return from_field("user","hash","username",username)[0][0]

def user_kitchen(userid):
    """ Return a dictionnary that contains kitchen of the user identified
    by userid. """

    kitchens = from_field('kitchen','name', 'user', userid)
    result = ({'name':k[0]} for k in kitchens) if kitchens else None
    return result

def authenticate(username):
    """ Insert the id of an authenticated user into the database. """
    uid = user_id(username)

    # This should not happen since we can only authenticate existing
    # user but just in case.
    if not uid:
        return

    param = (uid,)
    sql = "INSERT OR IGNORE INTO authenticated (id) values (?)"
    with sqlite3.connect(con_str) as con:
        con.execute(sql,param)
    return

def deauthenticate(username):
    """ Remove the entry relative to the given username in the authenticated
    table. """

    uid = user_id(username)
    param = (uid,)
    sql = "DELETE FROM authenticated where id=?"
    with sqlite3.connect(con_str) as con:
        con.execute(sql, param)
    return

def kitchen_create(userid, name):
    """ Insert a kitchen with name and associated with user id. """
    param = (name,userid)
    sql = "INSERT INTO kitchen (name, user) values (?,?)"
    with sqlite3.connect(con_str) as con:
        con.execute(sql, param)
    return

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

def from_id(tname, col_id):
    """ Returns all the column in tname table where the column id == col_id."""

    param = (col_id,)
    sql = "SELECT * from {0} where id=?".format(tname)
    with sqlite3.connect(con_str) as con:
        result = con.cursor().execute(sql, param).fetchone()
    return result

def from_field(tname, rname , fname, value):
    """ Returns the value of rname from tname where fname=value. """
    param = (value,)
    sql = "SELECT {0} from {1} where {2}=?".format(rname,tname,fname)
    with sqlite3.connect(con_str) as con:
        result = con.cursor().execute(sql, param).fetchall()
        result = result if result else None
    return result

if __name__ == '__main__':
    test()


