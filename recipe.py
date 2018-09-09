#!/usr/bin/env python3.6

'''Recipe handling'''

from collections import namedtuple
RecipeStep = namedtuple('recipe_step', 'number description')
Ingredient = namedtuple('ingredient', 'name amount unit')

UNITS = ["st", "g", "ml", "dl", "port"]

class Recipe:
    ''' Holds a recipe '''
    def __init__(self, title, servings=None, time=None, description=None):
        self.title = title
        self.servings = servings
        self.time = time
        self.description = description
        self.tags = []
        self.steps = []
        self.ingredients = []

    def add_instruction_step(self, description, number=None):
        ''' Add a recipe description step '''
        number = number if number is not None else len(self.steps) + 1
        self.steps.append(RecipeStep(number, description))

    def add_ingredient(self, ingredient_name, amount=None, unit=None):
        ''' Add an ingredient '''
        if unit and unit not in UNITS:
            print(f"wrong unit, valid: {UNITS}")
            return
        self.ingredients.append(Ingredient(ingredient_name, amount, unit))

    def add_tag(self, tag):
        ''' Add tag to recipe, used for searching '''
        self.tags.append(tag)
