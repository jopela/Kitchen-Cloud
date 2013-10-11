#!/usr/bin/env python
# The sqlite3 backend implementation of the database function.

import sqlite3

def test():
    """ used for testing ... NEEDS TO BE REPLACED BY SERIOUS TESTING """
    result = user_uname_exists("jopela")
    print result, type(result)
    return

# TODO: specify the database connection details in a config file or
# get it from the command line argument. For the moment, just hardcode in
# the app.
con_str ='../../db/kcdb'

def user_uname_exists(uname):
    """ returns True if this username exists in the database. False
    otherwise. """
    param = (uname,)
    sql = "SELECT count(*) from user where username=?"
    print "inside the func:",uname, type(uname)
    return cursor().execute(sql, param).fetchone()[0] == 1

##########################
# database helper methods.
##########################

def cursor():
    """ Handles connecting to the database and returns a cursor ready for
    execution. """
    conn = sqlite3.connect(con_str)
    cur = conn.cursor()
    return cur

if __name__ == '__main__':
    test()




