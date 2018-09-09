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
        return self._recipe_to_html(self.recipes[0])

    index.exposed = True

    def _recipe_to_html(self, rec):
        title = rec.title
        html = f"<h1>{title}</h1><br>\n"
        html += f"<b>{rec.servings} port | {rec.time} min</b><br>"
        html += self._ingredients_to_table(rec.ingredients)
        return html

    def _ingredients_to_table(self, ingredients):
        table = r"<table><tr><td>Ingredienser</td></tr>"
        for ing in ingredients:
            text = ing.name
            if ing.amount:
                text += f", {ing.amount}"
                if ing.unit:
                    text += f"{ing.unit}"
            table += f"<tr><td>{text}</td></tr>"
        return table + r"</table>"


RECIPES = []
REC = recipe.Recipe("Pasta med tonfisksås och sojabönor", 4, 15)
REC.add_ingredient("pasta", 4, "port")
REC.add_ingredient("tonfisk i burk", 2, "st")
REC.add_ingredient("sojabönor", 250, "g")
REC.add_ingredient("tomatpesto", 1, "dl")
REC.add_ingredient("matlagningsgrädde", 2.5, "dl")
REC.add_ingredient("ruccola", 75, "g")
REC.add_ingredient("salt och peppar")

json_tool.recipe_to_json_file(REC)

RECIPES.append(REC)

cherrypy.config.update({'server.socket_host': LAN_IP})
cherrypy.quickstart(HelloWorld(RECIPES))
