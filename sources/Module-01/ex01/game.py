class GotCharacter:
    """Game of thrones characters class"""
    def __init__(self, first_name=None, is_alive=None):
        self.first_name = 'No name' if first_name is None else first_name
        self.is_alive = True if is_alive is None else is_alive


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


class ThisIsAJoke(Lannister):
    """An undying class"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = 'This is a joke'
        self.house_words = 'We shall not die.'

    def die(self):
        print('Nothing to see here. We don\'t die !!')
