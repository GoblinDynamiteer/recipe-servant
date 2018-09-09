#!/usr/bin/env python3.6

''' Serves a CherryPy recipe site '''

import cherrypy
import recipe
import json_tool

LAN_IP = '192.168.0.193'


class HelloWorld(object):
    ''' CherryPy HelloWorld '''
    def __init__(self, recipes):
        self.recipes = recipes
    def index(self):
        ''' Index path'''
        return self.recipe_to_html(self.recipes[0])

    index.exposed = True

    def recipe_to_html(self, rec):
        title = rec.title
        html = f"<h1>{title}</h1><br>\n"
        html += f"{rec.servings} port | {rec.time} min"
        return html

RECIPES = []
REC = recipe.Recipe("Pasta med tonfisksås och sojabönor", 4, 15)

json_tool.recipe_to_json_file(REC)

RECIPES.append(REC)

cherrypy.config.update({'server.socket_host': LAN_IP})
cherrypy.quickstart(HelloWorld(RECIPES))
