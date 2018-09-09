#!/usr/bin/env python3.6

import cherrypy

LAN_IP = '192.168.0.193'

class HelloWorld(object):
    ''' CherryPy HelloWorld '''
    
    def index(self):
        ''' Index path'''
        return "Hello World!"

    index.exposed = True

cherrypy.config.update({'server.socket_host': LAN_IP})
cherrypy.quickstart(HelloWorld())
