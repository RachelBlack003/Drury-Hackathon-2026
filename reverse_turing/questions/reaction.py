import pygame
from moving_button import Button
from text_handler import Question_Text_handler
from textbox import Textbox
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
            x= randrange(50,750),
            y = randrange(40,500), 
            size = 30,
            padding=15,
            font_color= (0,0,0),
            bg_color= (230,230,230)
        )

        self.Text_handler = Question_Text_handler("quick_math")

        self.Textbox = Textbox(
            self.screen,
            text=self.Text_handler.get_text()
        )

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # might change to button
                self.done = True
                self.is_done()
        if event.type == pygame.MOUSEBUTTONDOWN and self.Text_handler.is_active():
            if self.Text_handler.is_active():
                text, _continue = self.Text_handler.next() #type: ignore
                if _continue:
                    self.Textbox.update_text(text)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.is_selected(event.pos):
                self.button.x = randrange(50,750),
                self.button.y = randrange(40,500),

        

    def update(self, fr):
        pass

    def draw(self, screen):
        self._render_title(screen)

    def _render_title(self, screen):
        if self.Text_handler.is_active():
            self.Textbox.render()
        else:
            text = self.font.render("Fifth Question", True, (255,255,255))
            screen.blit(text, (250, 300))
            self.button.render()

    def is_done(self):
        return self.done