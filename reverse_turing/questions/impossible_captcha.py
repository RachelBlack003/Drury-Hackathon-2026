import pygame
from pathlib import Path
from textbox import Textbox
from text_handler import Question_Text_handler
from captcha_button import Captcha_button

class ImpossibleCaptcha:
    def __init__(self, controller):
        self.controller = controller
        self.screen = controller.screen
        self.done = False
        self.font = pygame.font.SysFont(None, 40)

        self.Text_handler = Question_Text_handler("quick_math")

        self.Textbox = Textbox(
            self.screen,
            text=self.Text_handler.get_text()
        )

        image_path = Path(__file__).resolve().parent.parent / "assets" / "ManWaving.jpg"

        self.captcha_one = Captcha_button(
            screen = self.screen,
            img = str(image_path),
            x = 200,
            y = 200,
            width = 200,
            height = 200
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

    def is_done(self):
        return self.done