import pygame
import time
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

        self.button_presses = 0
        self.start_time = time.time()
        self.end_time = None

        self.required_speed = 10
        self.required_button_presses = 5

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

        self.Text_handler = Question_Text_handler("reaction")

        self.Textbox = Textbox(
            self.screen,
            text=self.Text_handler.get_text()
        )

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # might change to button
                self.done = True
                self.is_done()

        elif event.type == pygame.MOUSEBUTTONDOWN and self.Text_handler.is_active():
            if self.Text_handler.is_active():
                text, _continue = self.Text_handler.next() #type: ignore
                if _continue:
                    self.Textbox.update_text(text)
                elif self.Text_handler.is_final_text():
                    self.done = True
                    self.is_done()
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if self.button.is_selected(event.pos):

                if self.button_presses >= self.required_button_presses:
                    self.hande_results()
                    return
                
                self.button.x = randrange(50,750),
                self.button.y = randrange(40,500)
                
                self.button_presses += 1

    def hande_results(self):
        self.end_time = time.time()
        score = self.get_score()

        if score == 20:
            self.Text_handler.win()
            self.Textbox.update_text(self.Text_handler.get_text())
        else:
            self.Text_handler.lose()
            self.Textbox.update_text(self.Text_handler.get_text())
        self.controller.game.results.append(score)

    def get_score(self):
        score = 0
        if self.end_time - self.start_time <= self.required_speed:
            return 20
        else:
            return 0

    def update(self, fr):
        pass

    def draw(self, screen):
        if self.Text_handler.is_active():
            self.Textbox.render()
        else:
            self._render_title(screen)
            self.button.render()

    def _render_title(self, screen):
        text = self.font.render("Fifth Question", True, (255,255,255))
        screen.blit(text, (250, 300))

    def is_done(self):
        return self.done