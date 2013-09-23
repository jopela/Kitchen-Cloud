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

import web

# DEBUG FLAG (Set to False in prod).
web.config.debug = True

# Application urls mapping.
urls = (
    '/','index',
    '/login','login'
    )

render = web.template.render('templates/',base='base')

class index:
    def GET(self):
        return render.index()

class login:
    def GET(self):
        return render.login()

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()


