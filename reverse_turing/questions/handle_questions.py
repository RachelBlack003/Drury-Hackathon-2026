from state_manager.screen import Screen
import pygame

from questions.mouse_trajectory import MouseTrajectory
from questions.impossible_captcha import ImpossibleCaptcha
from questions.preference import Preference
from questions.quick_math import QuickMath
#from questions.(fifth_question file name) import (fifth_question class name)

class Handle_Questions(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.question_classes = [
            MouseTrajectory,
            ImpossibleCaptcha,
            Preference,
            QuickMath,
        ]

        self.question_index = 0
        self.current_question = self.question_classes[0](self)

    def next_question(self):
        self.question_index += 1

        if self.question_index >= len(self.question_classes):
            from state_manager.final_state import FinalEvaluation
            self.game.current_screen = FinalEvaluation(self.game)
        else:
            self.current_question = self.question_classes[self.question_index](self)

    def handle_event(self, event):
        self.current_question.handle_event(event)

    def update(self, dt):
        self.current_question.update(dt)

        if self.current_question.is_done():
            self.next_question()

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.current_question.draw(self.screen)