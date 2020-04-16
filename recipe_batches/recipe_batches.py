#!/usr/bin/python

# def recipe_maker(dictionary_recipe, dictionary_ingredients)

# dictionary_recipe = {ingredient_name: amount_needed}
# dictionary_ingredients = {ingredient_name: amount_available_to_me}

# ---------

# output the maximum number of whole batches that can be made for the supplied recipe

import math

def recipe_batches(recipe, ingredients):
	# if recipe is longer than ingredients return 0
	# keep a count of how many batches we can make
	# find the smallest ingredient we have in our supply, ingredients
	# keep subtracting by the recipe amount until we are in the negatives
	# return the count
	if len(recipe) > len(ingredients):
		return 0

	sm_ing_name, sm_ing_value = ("", math.inf)
	recipe_ing_value = math.inf

	for key, value in ingredients.items():
		if value < sm_ing_value:
			sm_ing_name, sm_ing_value = key, value
			try:
				recipe_ing_value = recipe[key]
			except Exception as e:
				return "recipe does not have this ingredient"

	return sm_ing_value // recipe_ing_value
	

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))