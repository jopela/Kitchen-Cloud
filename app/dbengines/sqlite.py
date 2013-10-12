#!/usr/bin/env python
# The sqlite3 backend implementation of the database function.
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

##########################
# database helper methods.
##########################
def field_exists(tname, fname, value):
    """ Returns True if value of fname exists in the table tname. False
    otherwise. """
    param = (value,)
    # sqlinjection arent a problem here because tname and fname are not
    # provided as user input but by the application. A case could surely be
    # made that this is still insecure but let's ignore it at this point.
    sql = "SELECT count(*) from {0} where {1}=?".format(tname, fname)
    return cursor().execute(sql, param).fetchone()[0] == 1


def cursor():
    """ Handles connecting to the database and returns a cursor ready for
    execution. """
    conn = sqlite3.connect(con_str)
    cur = conn.cursor()
    return cur

if __name__ == '__main__':
    test()




