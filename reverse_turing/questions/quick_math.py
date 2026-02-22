import pygame
from text_handler import Question_Text_handler
from textbox import Textbox

class QuickMath:
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

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.Text_handler.is_active():
            if self.Text_handler.is_active():
                text, _continue = self.Text_handler.next()
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
            text = self.font.render("Quick Math", True, (255,255,255))
            screen.blit(text, (250, 300))

    def is_done(self):
        return self.done