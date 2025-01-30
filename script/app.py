'''App encapsulates the program logic.'''

import locale

class App:
    '''App will do stuff!'''

    def __init__(self, screen):
        self.screen = screen
        self.width = 0
        self.height = 0
        self.init()

    def init(self):
        # Needed to correctly display symbols.
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        # Check dimensions.
        # start colours.

    def check(self):
        ...

    def start_colour(self):
        ...

    def create_ui(self):
        ...
        # Should UI be in its own class?

    def update_ui(self):
        ...

    def get_input(self):
        ...

    def do_stuff(self):
        ...
        # main logic goes here.
