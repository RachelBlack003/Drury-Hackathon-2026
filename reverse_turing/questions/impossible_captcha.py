import pygame
from pathlib import Path
from textbox import Textbox
from text_handler import Question_Text_handler
from captcha_button import Captcha_button
from button import Button

class ImpossibleCaptcha:
    def __init__(self, controller):
        self.controller = controller
        self.screen = controller.screen
        self.done = False
        self.font = pygame.font.SysFont(None, 40)

        self.Text_handler = Question_Text_handler("impossible_captcha")

        self.Textbox = Textbox(
            self.screen,
            text=self.Text_handler.get_text()
        )

        image_path = Path(__file__).resolve().parent.parent / "assets" / "ManWaving.jpg"

        self.captcha_one = Captcha_button(
            screen = self.screen,
            img = str(image_path),
            x = 150,
            y = 175,
            width = 150,
            height = 150
        )

        self.captcha_two = Captcha_button(
            screen = self.screen,
            img = str(image_path),
            x = 325,
            y = 175,
            width = 150,
            height = 150
        )

        self.captcha_three = Captcha_button(
            screen = self.screen,
            img = str(image_path),
            x = 500,
            y = 175,
            width = 150,
            height = 150
        )

        self.captcha_four = Captcha_button(
            screen = self.screen,
            img = str(image_path),
            x = 150,
            y = 350,
            width = 150,
            height = 150
        )

        self.captcha_five = Captcha_button(
            screen = self.screen,
            img = str(image_path),
            x = 325,
            y = 350,
            width = 150,
            height = 150
        )

        self.captcha_six = Captcha_button(
            screen = self.screen,
            img = str(image_path),
            x = 500,
            y = 350,
            width = 150,
            height = 150
        )

        self.Pass = Button(
            screen = self.screen,
            text = "Pass", 
            x= 600,
            y = 600, 
            size = 30,
            padding=15,
            font_color= (0,0,0),
            bg_color= (230,230,230)
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.Text_handler.is_active():
            if self.Text_handler.is_active():
                text, _continue = self.Text_handler.next() # type: ignore
                if _continue:
                    self.Textbox.update_text(text)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # might change to button
                self.done = True
                self.is_done()

    def update(self, dt):
        pass

    def draw(self, screen):
        if self.Text_handler.is_active():
            self.Textbox.render()
        else:
            text = self.font.render("Impossible Captcha", True, (255,255,255))
            screen.blit(text, (250, 300))
            self.captcha_one.render()
            self.captcha_two.render()
            self.captcha_three.render()
            self.captcha_four.render()
            self.captcha_five.render()
            self.captcha_six.render()
            self.Pass.render()

    def is_done(self):
        return self.done