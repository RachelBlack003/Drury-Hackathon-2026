from state_manager.screen  import Screen
from button import Button
import pygame

class TitleScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont(None, 60)

        self.start_button = Button(
            screen = self.game.screen,
            text = "Start", 
            x= 400,
            y = 500, 
            size = 40,
            padding= 15
            
        )

        self.abort_button = Button(
            screen = self.game.screen,
            text = "Abort", 
            x=400,
            y = 600, 
            size = 40,
            padding=15
        )

    def start_game(self):
        from state_manager.intro_screen import IntroScreen
        self.game.current_screen = IntroScreen(self.game)


    def abort(self):
        self.game.running = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.is_selected(event.pos):
                self.start_game()

            if self.abort_button.is_selected(event.pos):
                self.game.running = False

    def draw(self):
        self.screen.fill((200,200,200))

        title = self.font.render("Reverse Turing Test", False, (255,255,255))
        self.screen.blit(title, (200, 200))
  
        self.start_button.render()
        self.abort_button.render()