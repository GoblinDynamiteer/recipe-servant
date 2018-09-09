#!/usr/bin/env python3.6

''' Serves a CherryPy recipe site '''

import cherrypy
import recipe

LAN_IP = '192.168.0.193'



class HelloWorld(object):
    ''' CherryPy HelloWorld '''
    def __init__(self, recipes):
        self.recipes = recipes
    def index(self):
        ''' Index path'''
        return self.recipe_to_html(self.recipes[0])

    index.exposed = True

    def recipe_to_html(self, recipe_to_convert):
        title = recipe_to_convert.title
        html = f"<h1>{title}</h1><br>\n"
        html += f"Placeholder text"
        return html

RECIPES = []
REC = recipe.Recipe("Pasta med tonfisksås och sojabönor", 4, 15)

RECIPES.append(REC)

cherrypy.config.update({'server.socket_host': LAN_IP})
cherrypy.quickstart(HelloWorld(RECIPES))
