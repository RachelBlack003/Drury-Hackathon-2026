from game import Game
from state_manager.title_screen import TitleScreen

WIDTH, HEIGHT = 800, 800

if __name__ == "__main__":
    game = Game(WIDTH, HEIGHT)
    game.current_screen = TitleScreen(game)
    game.run()