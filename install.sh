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

mkdir -p ${DBPATH}
touch ${DBFILE}

sqlite3 ${DBFILE} < ${SCHEMAPATH}/schema.sql

# All done.
echo "Installation Completed"




