#!/usr/bin/env python
#coding:utf-8

import sys
sys.path.append("%s/common" % sys.path[0])

import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.options import define,options

from application import application

define("port",default=8088,help="run on th given port",type=int)
options.logging = "debug"

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print 'Development server is running at http://127.0.0.1:%s/tornado' % options.port
    print 'Quit the server with Control-C'
    tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
    main()
