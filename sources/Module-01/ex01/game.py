class GotCharacter:
    """Game of thrones characters class"""
    def __init__(self, first_name=None, is_alive=None, killed_enemies=None):
        self.first_name = first_name
        self.is_alive = True if is_alive is None else is_alive
        self.killed_enemies = 0 if killed_enemies is None else killed_enemies

    def kill(self, enemy: "GotCharacter"):
        if self == enemy:
            print('Suicide is not allowed !')
        elif isinstance(enemy, Undying):
            print('Sorry, you can\'t kill the undying!')
        elif enemy.is_alive is True:
            print(f'{self.first_name} stabbed {enemy.first_name} to death.')
            enemy.is_alive = False
            self.killed_enemies += 1
        else:
            print('Enemy already dead, you\'re cheating!\nPenalty received.')
            self.killed_enemies -= 1

    def __str__(self):
        return(f"I, called {self.first_name}, am \
{'alive !' if self.is_alive is True else 'dead :(.'} \
I already killed {self.killed_enemies} person.")


class Lannister(GotCharacter):
    """The Lannister's class.. unless they're not classy"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = 'Lannister'
        self.house_words = 'Hear Me Roar!'

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

    def __str__(self):
        return super().__str__() + f'\nI\'m from the {self.family_name} \
family. My moto is {self.house_words}.'


class GracefordofHolyhall(GotCharacter):
    """The Graceford of Holygraph's class.. oups, Holyhall"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = 'The graceford of Holyhall'
        self.house_words = 'Hear Me Roar!'

    def print_house_words(self):
        print(self.house_words)

    def print_whoarewe(self):
        print(f'I\'m {self.first_name} from {self.family_name}')

    def die(self):
        self.is_alive = False

    def __str__(self):
        return super().__str__() + f'\nI\'m from the {self.family_name} \
family. My moto is {self.house_words}.'


class Undying(GotCharacter):
    """An undying class"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = 'Undying'
        self.house_words = 'We shall not die.'

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        print('Nothing to see here. We don\'t die !!')

    def __str__(self):
        return super().__str__() + f'\nI\'m from the {self.family_name} \
family. My moto is {self.house_words}.'
