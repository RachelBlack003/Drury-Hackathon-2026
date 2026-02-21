import pygame
from text_handler import Question_Text_handler
from textbox import Textbox

class QuickMath:
    def __init__(self, controller):
        self.controller = controller
        self.screen = controller.screen
        self.done = False
        self.font = pygame.font.SysFont(None, 40)

        # self.Text_handler = Text_handler()

        self.Textbox = Textbox(
            self.screen,
            text="Initial text"
        )

    def handle_event(self, event):
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     self.Textbox.update_text(self.Text_handler.test_lines[0])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # might change to button
                self.done = True
                self.is_done()

    def update(self, dt):
        pass

    def draw(self, screen):
        text = self.font.render("Quick Math", True, (255,255,255))
        screen.blit(text, (250, 300))
        self.Textbox.render()

    def is_done(self):
        return self.done