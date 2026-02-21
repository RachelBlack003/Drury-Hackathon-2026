""" Base class just for inherence of children screens """

class Screen:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

    def handle_event(self, event):
        raise NotImplementedError

    def update(self, dt):
        pass

    def draw(self):
        raise NotImplementedError