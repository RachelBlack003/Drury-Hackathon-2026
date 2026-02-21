import pygame
from captcha_button import Captcha_button

class ImpossibleCaptcha:
    def __init__(self, controller):
        self.controller = controller
        self.screen = controller.screen
        self.done = False
        self.font = pygame.font.SysFont(None, 40)

        self.captcha_one = Captcha_button(
            screen = self.screen,
            img = "reverse_turing/assets/ManWaving.jpg",
            x = 200,
            y = 200,
            width = 200,
            height = 200
        )

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # might change to button
                self.done = True
                self.is_done()

    def update(self, dt):
        pass

    def draw(self, screen):
        text = self.font.render("Impossible Captcha", True, (255,255,255))
        screen.blit(text, (250, 300))
        self.captcha_one.render()

    def is_done(self):
        return self.done