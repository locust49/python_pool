def assertion_required_argument(argument):
    return f'Recipe().__init__() missing 1 required positional argument: \
{argument}'


def assertion_input_error(argument):
    if argument == 'cooking_lvl':
        return '\'cooking level\' must be in range [1, 5].'
    if argument == 'cooking_time':
        return '\'cooking_time\' must be a positive number (int).'
    if argument == 'ingredients':
        return '\'ingredients\' must be a list of strings.'
    if argument == 'recipe_type':
        return '\'recipe_type\' can only be \
    \b\'starter\', \'lunch\' or \'dessert\''
    return 'Invalid input'


class Recipe():
    def __init__(self, name=None, cooking_lvl=None, cooking_time=None,
                 ingredients=None, description=None, recipe_type=None):
        try:
            assert name, assertion_required_argument('name')
            assert cooking_lvl, assertion_required_argument('cooking_lvl')
            assert cooking_time, assertion_required_argument('cooking_time')
            assert ingredients, assertion_required_argument('ingredients')
            assert recipe_type, assertion_required_argument('recipe_type')

            assert cooking_lvl in range(1, 6),                          \
                   assertion_input_error('cooking_lvl')
            assert type(cooking_time) == int and cooking_time >= 0,     \
                   assertion_input_error('cooking_time')
            assert type(ingredients) == list and                        \
                   all(isinstance(item, str) for item in ingredients),  \
                   assertion_input_error('ingredients')
            assert recipe_type in ['starter', 'lunch', 'dessert'],      \
                   assertion_input_error('recipe_type')
        finally:
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = 'No description available for this recipe.'  \
                if description is None else description
            self.recipe_type = recipe_type

    def __str__(self):
        return 'Recipe name\t\t:  {name}\n\
Recipe cooking level\t:  {cooking_lvl}\n\
Recipe cooking time\t:  {cooking_time}\n\
Recipe ingredients\t:  {ingredients}\n\
Recipe description\t:  {description}\n\
Recipe recipe type\t:  {recipe_type}'.format(**self.__dict__)
