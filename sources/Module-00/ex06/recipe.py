cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10,
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60,
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15,
    },
}


def print_keys(dictionnary, prefix=None):
    for key in dictionnary:
        if prefix is not None:
            print(prefix, key)
        else:
            print(key)


def print_values(dictionnary):
    for key in dictionnary:
        print(dictionnary[key])


def print_items(dictionnary):
    for key in dictionnary:
        print(key, ':', dictionnary[key])


def print_recipe(recipe_name):
    if recipe_name in cookbook:
        print(f"Recipe for {recipe_name}:\n\
Ingredients list: {cookbook[recipe_name]['ingredients']}\n\
To be eaten for {cookbook[recipe_name]['meal']}.\n\
Takes {cookbook[recipe_name]['prep_time']} minutes of cooking.")
    else:
        print('Meal not found. Operation skipped.')


def delete_recipe(recipe_name):
    print('Would you like to delete {} from the cookbook? [yes/No] '
          .format(recipe_name))
    answer = input()
    if answer == 'yes' or answer == 'y' or answer == 'Y':
        if recipe_name in cookbook:
            del cookbook[recipe_name]
            print('Meal deleted from cookbook successfully.')
        else:
            print('Meal not found. Operation skipped.')
    elif answer == 'no' or answer == 'n' or answer == 'N':
        print('Okay then. :)')
    else:
        print('Not supported input. Operation skipped.')


def add_recipe(recipe_name, ingredients, meal, prep_time):
    recipe = {recipe_name: {'ingredients': ingredients,
              'meal': meal, 'prep_time': prep_time}}
    if recipe_name in cookbook:
        print('Meal already exists. Are you sure you want \
to overwrite it ? [yes/No] ')
        answer = input()
        if answer not in ['yes', 'y', 'Y']:
            return
        cookbook.update(recipe)
    else:
        cookbook.update(recipe)


def print_cookbook():
    print('-' * 42)
    print('{:->21}{:-<21}'.format('COOK', 'BOOK'))
    print('-' * 42)
    print_keys(cookbook, '🍽 ')
    print('-' * 42)
    print('-' * 42)


def get_recipe():
    print('What\'s the recipe name?')
    recipe_name = input()
    print('Insert the ingredients of the recipe (1 line separated by spaces)')
    recipe_ingredients = list(input().split())
    print('When do you eat this meal ? [breakfast/lunch/dinner/dessert ...]')
    recipe_meal = input()
    print('How much time does it take to prepare this meal (in minutes)?')
    recipe_prep_time = input()
    while recipe_prep_time.isnumeric() is not True:
        print('Please, insert a valid preparation time (Only numbers)')
        recipe_prep_time = input()
    add_recipe(recipe_name, recipe_ingredients, recipe_meal,
               int(recipe_prep_time))


def menu():
    menu = {
            1: 'Add a recipe',
            2: 'Delete a recipe',
            3: 'Print a recipe',
            4: 'Print the cookbook',
            5: 'Quit'
    }
    print_items(menu)
    choice = input('Please select an option by typing the corresponding \
number:')
    while (choice not in [1, 2, 3, 4, 5]):
        if choice.isnumeric() and int(choice) < 6 and int(choice) > 0:
            choice = int(choice)
            if choice == 1:
                get_recipe()
                print('Meal added to cookbook successfully.')
            elif choice == 2:
                delete_recipe(input('Insert meal name : '))
            elif choice == 3:
                print_recipe(input('Please enter the recipe\'s name \
to get its details: '))
            elif choice == 4:
                if len(cookbook) == 0:
                    print('The cookbook is empty. Why don\'t you add \
some recipes?')
                else:
                    print_cookbook()
            elif choice == 5:
                print('Cookbook closed.')
                break
        else:
            print_items(menu)
            choice = input('Please select an option by typing the \
corresponding number:')


menu()
