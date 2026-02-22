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

        self.captcha_buttons = []
        positions = [
            (150, 175), (325, 175), (500, 175),
            (150, 350), (325, 350), (500, 350)
        ]

        for x, y in positions:
            self.captcha_buttons.append(
                Captcha_button(
                    screen=self.screen,
                    img=str(image_path),
                    x=x,
                    y=y,
                    width=150,
                    height=150
                )
            )

        self.Pass = Button(
            screen=self.screen,
            text="Pass",
            x=600,
            y=600,
            size=30,
            padding=15,
            font_color=(0, 0, 0),
            bg_color=(230, 230, 230)
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.Text_handler.is_active():
            if self.Text_handler.is_active():
                text, _continue = self.Text_handler.next()
                if _continue:
                    self.Textbox.update_text(text)
                elif self.Text_handler.is_final_text():
                    self.done = True
                    self.is_done()


        if event.type == pygame.MOUSEBUTTONDOWN and not self.soft_done:
            for button in self.captcha_buttons:
                if button.is_selected(event.pos):
                    button.toggle()
                    return

            if self.Pass.is_selected(event.pos):
                self.evaluate_captcha()
                return

        if event.type == pygame.MOUSEBUTTONDOWN and self.soft_done:
            self.done = True

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
                
    def evaluate_captcha(self):

        self.submitted = True

        any_selected = any(button.selected for button in self.captcha_buttons)

        if any_selected:
            self.lose()
        else:
            self.win()

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
        for button in self.captcha_buttons:
            button.render()

        self.Pass.render()

    def is_done(self):
        return self.done