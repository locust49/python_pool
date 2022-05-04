from tkinter.ttk import Separator
from recipe import Recipe
from book import Book
import sys


sys.tracebacklimit = 0
dashed_line = 39 * '--' + '\n'

if len(sys.argv) < 2:
    book = Book('Tasty recipes')
    print(f'{dashed_line}{book}')
    print('>> Instanciate Recipes.')
    coffee = Recipe('Latte Coffee', 1, 15, ['brewed dark roast espresso',
                    'milk'], 'Tasty coffee to shine in a Monday morning.',
                    'starter')
    pancake = Recipe('Pancakes', 3, 20, ['all-purpose flour', 'baking powder',
                     'salt', 'white sugar', 'milk', 'egg', 'melted butter'],
                     'This is a great recipe that I found in my Grandma\'s \
recipe book. Judging from the weathered look of this \
recipe card, this was a family favorite.', 'lunch')
    juice = Recipe('Blueberry smoothie recipe', 1, 5, ['blueberries', 'banana',
                   'yogurt', 'apple juice', 'mint leaves'],
                   recipe_type='dessert')
    icecream = Recipe('Vanilla ice cream', 1, 60, ['heavy cream', 'whole milk',
                      'sugar', 'salt', 'vanilla extract'],
                      recipe_type='dessert')
    print(f'{dashed_line}{coffee}')
    print(f'{dashed_line}{pancake}')
    print(f'{dashed_line}{juice}')
    print(f'{dashed_line}{icecream}')
    print(dashed_line, end='')
    print('>> books.add_recipe(Recipe):')
    book.add_recipe(coffee)
    book.add_recipe(pancake)
    book.add_recipe(icecream)
    print(f'{dashed_line}{book}')
    book_s = Book('book2')
    print(f'{dashed_line}{book_s}')
    book_s.add_recipe(juice)
    book.add_recipe(juice)
    print(f'{dashed_line}{book_s}')
    print(f'{dashed_line}{book}')
    print(dashed_line, end='')
    print('>> books.get_recipe_by_name(\'dessert\'):')
    book.get_recipe_by_name('Latte Coffee')
    book_s.get_recipe_by_name('Latte Coffee')
    print(dashed_line, end='')
    print('>> books.get_recipes_by_types(\'dessert\'):')
    print(book.get_recipes_by_types('dessert'))
    print(book_s.get_recipes_by_types('dessert'))
    print('>> books.get_recipes_by_types(\'starter\'):')
    print(book.get_recipes_by_types('starter'))
    print(book_s.get_recipes_by_types('starter'))
    print(dashed_line, end='')
elif len(sys.argv) == 2 and sys.argv[1] == '--errors':
    print(f'>> Testing erros cases || Comment to check next error <<\n\
{dashed_line}')
    print('Recipe Name errors:\n')
    noname = Recipe(name=None, cooking_lvl=10, cooking_time=20,
                    ingredients=['ingre'], description='desc',
                    recipe_type='starter')
    print('Recipe cooking level errors:\n')
    nocooking_lvl = Recipe(name='recipe\'s name', cooking_lvl=None,
                           cooking_time=20, ingredients=['ingre'],
                           description='desc', recipe_type='starter')
    notinrange_cooking_lvl = Recipe(name='recipe\'s name', cooking_lvl=10,
                                    cooking_time=20, ingredients=['ingre'],
                                    description='desc', recipe_type='starter')
    wrongtype_cooking_lvl = Recipe(name='recipe\'s name', cooking_lvl=4.5,
                                   cooking_time=20, ingredients=['ingre'],
                                   description='desc', recipe_type='starter')
    print('Recipe cooking time errors:\n')
    no_cooking_time = Recipe(name='recipe\'s name', cooking_lvl=4,
                             cooking_time=None, ingredients=['ingre'],
                             description='desc', recipe_type='starter')
    notinrange_cooking_time = Recipe(name='recipe\'s name', cooking_lvl=4,
                                     cooking_time=-20, ingredients=['ingre'],
                                     description='desc', recipe_type='starter')
    print('Recipe ingredients errors:\n')
    no_ingredients = Recipe(name='recipe\'s name', cooking_lvl=4,
                            cooking_time=20, ingredients=None,
                            description='desc', recipe_type='starter')
    empty_ingredients = Recipe(name='recipe\'s name', cooking_lvl=4,
                               cooking_time=20, ingredients=[],
                               description='desc', recipe_type='starter')
    wrongtype_ingredients = Recipe(name='recipe\'s name', cooking_lvl=4,
                                   cooking_time=20, ingredients=[1, 2, 3],
                                   description='desc', recipe_type='starter')
    print('Recipe recipe_type errors:\n')
    no_recipe_type = Recipe(name='recipe\'s name', cooking_lvl=4,
                            cooking_time=20, ingredients=['ingreds', '...'],
                            description='desc', recipe_type=None)
    wrong_recipe_type = Recipe(name='recipe\'s name', cooking_lvl=4,
                               cooking_time=20, ingredients=['ingreds', '...'],
                               description='desc', recipe_type=1)
    mybook = Book('my beautiful Book')
    print(f'{dashed_line}{mybook}\n{dashed_line}')
    print('Book add_recipe errors:\n')
    mybook.add_recipe('this is not a recipe')
else:
    print('Invalid args.')
