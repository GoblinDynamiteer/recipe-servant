#!/usr/bin/env python3.6

import os
import json


def recipe_to_json_file(rec):
    ''' Converts a recipe to a .json file in ./recipes/ '''
    file_name = _recipe_title_to_filename(rec.title)
    recipe_dict = _recipe_to_dict(rec)
    this_dir = os.path.dirname(__file__)
    recipe_dir = os.path.join(this_dir, "recipes")
    if not os.path.exists(recipe_dir):
        os.makedirs(recipe_dir)
    with open(f"recipes/{file_name}.json", 'w') as json_recipe_file:
        json.dump(recipe_dict, json_recipe_file)


def _recipe_to_dict(rec):
    recipe_dict = {"title" : rec.title}
    recipe_dict["steps"] = rec.steps
    recipe_dict["ingredients"] = rec.ingredients
    recipe_dict["time"] = rec.time
    recipe_dict["servings"] = rec.servings
    recipe_dict["description"] = rec.description
    return recipe_dict


def _recipe_title_to_filename(title: str):
    file_name = title.lower()
    file_name = file_name.replace(" ", "-")
    return file_name
