import pygame
from moving_button import Button
from random import randrange

class Reaction:
    def __init__(self, controller):
    
        self.controller = controller
        self.screen = controller.screen
        self.done = False

        self.font = pygame.font.SysFont(None, 40)

        self.button = Button(
            screen = self.screen,
            text = "Click here", 
            x=randrange(50,750),
            y = randrange(40,500), 
            size = 30,
            padding=15,
            font_color= (0,0,0),
            bg_color= (230,230,230)
        )

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # might change to button
                self.done = True
                self.is_done()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.is_selected(event.pos):
                self.button.x=randrange(50,750),
                self.button.y = randrange(40,500),

        

    def update(self, fr):
        pass

    def draw(self, screen):
        self._render_title(screen)

    def _render_title(self, screen):
        text = self.font.render("Fifth Question", True, (255,255,255))
        screen.blit(text, (250, 300))
        self.button.render()

    def is_done(self):
        return self.done