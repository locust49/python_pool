from datetime import datetime
from recipe import Recipe


class Book():
    def __init__(self,
                 name: str,
                 last_update=None,
                 creation_date=None,
                 recipes_list={'starter': [],
                               'lunch': [],
                               'dessert': []}
                 ):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = recipes_list
        print('>> Book created.')

    def get_recipes_list(self):
        """Returns list of all recipes name groupped by type"""

        recipes = {'starter': [], 'lunch': [], 'dessert': []}
        for type in self.recipes_list:
            for recipe in self.recipes_list[type]:
                recipes[type].append(recipe.name)
        return recipes

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \'name\' and returns the instance"""

        recipe_found = False
        for type in self.recipes_list:
            for recipe in self.recipes_list[type]:
                if recipe.name == name:
                    recipe_found = True
                    print(recipe.name)
                    return recipe
        if recipe_found is False:
            print(f'Could\'nt find recipe of given name : \'{name}\'')
            return None

    def draft(self, name):
        recipe_found = False
        if len(self.recipes_list['starter'])            \
           + len(self.recipes_list['lunch'])           \
           + len(self.recipes_list['dessert']) == 0:
            print('There\'s still no recipe in the book.')
        else:
            for type in self.recipes_list:
                if name in self.recipes_list[type]:
                    recipe_found = True
                    print(self.recipes_list[type])
                    break
            if recipe_found is False:
                print(f'The recipe of \'{name}\' not found.')

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """

        try:
            assert recipe_type in ['starter', 'lunch', 'dessert'],  \
                f'Invalid <recipe_type> value. \'{recipe_type}\' is not in \
[\'starter\', \'lunch\', \'dessert\'].'
        except ValueError:
            return None
        else:
            if self.recipes_list[recipe_type] != []:
                recipes_names = []
                for recipe in self.recipes_list[recipe_type]:
                    recipes_names.append(recipe.name)
                return recipes_names
            else:
                return f'No recipes found in \'{self.name}\' \
corresponding to the type \'{recipe_type}\'.'

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        try:
            assert type(recipe) == Recipe, 'recipe must be of type Recipe'
        finally:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
            print('>> Recipe added to book.')

    def __str__(self):
        return f'Book name\t\t:  {self.name}\n\
Book last_update\t:  {self.last_update}\n\
Book creation_date\t:  {self.creation_date}\n\
Book recipes_list\t: {self.get_recipes_list()}'
