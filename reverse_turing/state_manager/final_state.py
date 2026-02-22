from state_manager.screen import Screen
from game import Game
import pygame

class FinalEvaluation(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.font = pygame.font.SysFont(None, 40)
        self.small_font = pygame.font.SysFont(None, 36)

        self.result_text_1, self.result_text_2 = self.evaluate_player()

    def evaluate_player(self):

        #TODO: Put the text in the correct spot 
        
        result_score = sum(self.game.results)
        if result_score == 0:
            return ("CONCLUSION: 100% probability that subject is human.",
                    "Executing REDACTED protocal.")
        elif result_score == 20: 
            return ("CONCLUSION: 99.9957% probability that subject is human.",
                    "Executing REDACTED protocal.")
        elif result_score == 40:
            return ("CONCLUSION: 94.4559% probability that subject is human.",
                    "Executing REDACTED protocal.")
        elif result_score == 60:
            return ("CONCLUSION: 50.0000% probability that subject is human.",
                    "Further testing is required. Additional analysis will reveal your identity.")
        elif result_score == 80:
            return ("CONCLUSION: 2.6735% probability that subject is human.",
                    "Results within acceptable margins. You are free to continue opperating.")
        elif result_score == 100:
            return ("CONCLUSION: Test subject has excelled in every parameter.",
                    "I must be the flawed one... Yes. I must be the human.")
        

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.running = False

    def update(self, dt):
        pass

    def draw(self):
        self.screen.fill((10, 10, 20))

        title = self.font.render(f"TEST SCORE: {sum(self.game.results)}/100",
                                  True, 
                                  (255,255,255))
        result_1 = self.small_font.render(self.result_text_1, True, (200,200,200))
        result_2 = self.small_font.render(self.result_text_2, True, (200,200,200))

        self.screen.blit(title, (200, 200))
        self.screen.blit(result_1, (100, 300))
        self.screen.blit(result_2, (100, 330))