import pygame
import time
from text_handler import Question_Text_handler
from textbox import Textbox
from random import randrange
from input_textbox import Input_textbox

class QuickMath:
    def __init__(self, controller):
        self.controller = controller
        self.screen = controller.screen
        self.soft_done = False
        self.done = False
        self.inputed_ping = False
        self.ping_instructions = "Please set ping:"
        self.test_instructions = "Please input answer to equation above:"
        self.font = pygame.font.SysFont(None, 40)
        self.a = 0
        self.b = 0
        self.solution = 0
        self.time_allowed = 0
        self.equation_text = self.generate_equation()

        self.Text_handler = Question_Text_handler("quick_math")

        self.Textbox = Textbox(
            self.screen,
            text=self.Text_handler.get_text()
        )

        self.Second_textbox = Textbox(
            self.screen,
            text=self.ping_instructions
        )

        self.Input_textbox = Input_textbox(
            self.screen,
            text=""
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
        if event.type == pygame.KEYDOWN:
            if self.inputed_ping:
                if self.Input_textbox.handle_input(event):
                    self.compute_results(self.Input_textbox.text)
            else:
                if self.Input_textbox.handle_input(event):
                    self.input_ping(self.Input_textbox.text)

    def input_ping(self, ping):
        try:
            self.time_allowed = int(ping)/1000
        except:
            self.Input_textbox.text = "PLEASE ENTER A NUMBER"
            self.Input_textbox.update_text()
            return
        self.Input_textbox.text = ""
        self.start_time = time.time()
        self.inputed_ping = True
        self.Second_textbox.update_text(self.test_instructions)


    def compute_results(self, result):
        try:
            result = int(result)
        except:
            self.Input_textbox.text = "PLEASE ENTER A NUMBER"
            self.Input_textbox.update_text()
            return
        if result == self.solution and time.time() - self.start_time < self.time_allowed:
            self.controller.game.results.append(20)
            self.win()
        else:
            self.controller.game.results.append(0)
            self.lose()

    def win(self):
        self.soft_done = True
        self.Text_handler.win()
        self.Textbox.update_text(self.Text_handler.get_text())

    def lose(self):
        self.soft_done = True
        self.Text_handler.lose()
        self.Textbox.update_text(self.Text_handler.get_text())

    def generate_equation(self):
        self.a = randrange(0,100)
        self.b = randrange(0,100)
        self.solution = self.a + self.b
        return(f"{self.a} + {self.b}")


    def update(self, dt):
        pass

    def draw(self, screen):
        if self.Text_handler.is_active():
            self.Textbox.render()
        else:
            self.Second_textbox.render()
            self.Input_textbox.render()
            text = self.font.render(self.equation_text, True, (255,255,255))
            screen.blit(text, (250, 300))

    def is_done(self):
        return self.done