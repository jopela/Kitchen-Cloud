#!/bin/bash
# Kichen-Cloud installation script.
# Copyright (C) 2013  Jonathan Pelletier (jonathan.pelletier@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# create a database file and install the sql schema.

DBPATH=../db
SCHEMAPATH=./app/schema
DBNAME=kcdb
DBFILE=${DBPATH}/${DBNAME}
SCHEMAFILENAME=schema.sql
SEEDFILENAME=seeds.sql
DEBUG=true

# Clear the previous schema if in debug mode.
if [ $DEBUG ]; then
    echo 'Clearing the old schema ($DEBUG=true)'
    cat /dev/null > ${DBFILE}
fi

mkdir -p ${DBPATH}
touch ${DBFILE}

# Create the schema
echo "Installing the Schema"
sqlite3 ${DBFILE} < ${SCHEMAPATH}/${SCHEMAFILENAME}

# Quit if it fails.
if [ $? -ne 0 ]; then
    echo "Error creating sql schema. Please verify ${SCHEMAFILENAME} for errors"
    exit -1
fi

# Seed the database with values needed before app startup (e.g: list of 
# country codes, iso language codes etc.).
if [ -n "${SEEDFILENAME}" ]; then
    echo "Seeding the database ..."
    sqlite3 ${DBFILE} < ${SCHEMAPATH}/${SEEDFILENAME}

    if [ $? -ne 0 ]; then
        echo "Error seeding the database. Please verify ${SEEDFILENAME} for errors"
        exit -1
    fi
fi

# All done.
if [ $? -eq 0 ]; then
    echo "Installation Completed !"
else
    echo "Errors during the installation"
    exit -1
fi

exit 0



