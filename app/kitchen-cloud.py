#!/usr/bin/python2

import web

# Application urls mapping.
urls = (
    '/','index'
    )


class index:

    def GET(self):
        return "kitchen-cloud: work in your kitchen, manage it in the cloud!"


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
