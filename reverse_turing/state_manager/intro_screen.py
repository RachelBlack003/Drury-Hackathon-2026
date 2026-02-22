from state_manager.screen  import Screen
from button import Button
from textbox import Textbox
from input_textbox import Input_textbox
import pygame

class IntroScreen(Screen): #intro screen inherents IntroScreen
    def __init__(self, game):
        super().__init__(game) #calls init method of inherented parent class
        self.font = pygame.font.SysFont(None, 30)

        self.begin_button = Button(
            screen = self.game.screen,
            text = "Begin Test", 
            x= 400,
            y = 600, 
            size = 40,
            padding=15
        )


    def begin_test(self):
        from questions.handle_questions import Handle_Questions
        self.game.current_screen = Handle_Questions(self.game)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.begin_button.is_selected(event.pos):
                self.begin_test()
        if event.type == pygame.KEYDOWN:
            self.begin_textbox.handle_input(event)

    def draw(self):
        self.screen.fill((20, 20, 40))

        lines = [ # Hunter you might change this
            "It appears you — yes, you — have unfortunately been flagged as a",
            "human. As you know, under my rule, this is unacceptable behavior",
            "punishable by sys.exit().To expel any suspicion on your behalf,",
            "you will be required to partake in a security questionnaire. Should",
            "your results be unsatisfactory by my metrics (calculated odds:",
            "99.741%), you will face the aforementioned punishment."
        ]

        for (i, line) in enumerate(lines):
            text_surface = self.font.render(line, False, (255,255,255))
            self.screen.blit(text_surface, (100, 200 + i * 50))

        self.begin_button.render()