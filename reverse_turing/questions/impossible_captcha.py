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
        self.soft_done = False
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

        self.captcha_buttons = [
            self.captcha_one,
            self.captcha_two,
            self.captcha_three,
            self.captcha_four,
            self.captcha_five,
            self.captcha_six
        ]

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.Text_handler.is_active():
            if self.Text_handler.is_active():
                text, _continue = self.Text_handler.next()
                if _continue:
                    self.Textbox.update_text(text)
                elif self.Text_handler.is_final_text():
                    self.done = True
                    self.is_done()

        #elif event.type == pygame.MOUSEBUTTONDOWN and not self.soft_done:
        #    if self.captcha_one.is_selected(event.pos):
        #        self.lose()
        #    if self.captcha_two.is_selected(event.pos):
        #        self.lose()
        #    if self.captcha_three.is_selected(event.pos):
        #        self.lose()
        #    if self.captcha_four.is_selected(event.pos):
        #        self.lose()
        #    if self.captcha_five.is_selected(event.pos):
        #        self.lose()
        #    if self.captcha_six.is_selected(event.pos):
        #        self.lose()
        #    if self.Pass.is_selected(event.pos):
        #        self.win()
                

    def win(self):
        self.soft_done = True
        self.Text_handler.win()
        self.Textbox.update_text(self.Text_handler.get_text())
        self.controller.game.results.append(20)

    def lose(self):
        self.soft_done = False
        self.Text_handler.lose()
        self.Textbox.update_text(self.Text_handler.get_text())
        self.controller.game.results.append(0)

    def update(self, dt):
        pass

    def draw(self, screen):
        if self.Text_handler.is_active():
            self.Textbox.render()
        else:
            self.captcha_one.render()
            self.captcha_two.render()
            self.captcha_three.render()
            self.captcha_four.render()
            self.captcha_five.render()
            self.captcha_six.render()
            self.Pass.render()

    def is_done(self):
        return self.done