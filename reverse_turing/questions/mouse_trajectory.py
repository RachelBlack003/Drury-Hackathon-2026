from typing import Tuple

import pygame
import random 
import math

from text_handler import Question_Text_handler
from textbox import Textbox

class MouseTrajectory:
    def __init__(self, controller):
    
        self.controller = controller
        self.screen = controller.screen
        self.done = False

        self.font = pygame.font.SysFont(None, 40)

        #random box 
        self.rect_size = 60
        self.rect_x = random.randint(100, 700)
        self.rect_y = random.randint(100, 500)
        self.rect = pygame.Rect(
            self.rect_x,
            self.rect_y,
            self.rect_size, 
            self.rect_size
        )

        self.mouse_pos = []
        self.started = False
        self.start_pos: Tuple[int, int] | None= None
        self.collected_score = False
        self.direction_errors = []

        self.finish_timer = 0


        self.Text_handler = Question_Text_handler("preference")

        self.Textbox = Textbox(
            self.screen,
            text=self.Text_handler.get_text()
        )

    def handle_event(self, event):

        #Text Handling
        if self.Text_handler.is_active():
            if event.type == pygame.MOUSEBUTTONDOWN:
                text, _continue = self.Text_handler.next() #type: ignore
                if _continue:
                    self.Textbox.update_text(text)
            return  

        #Trajectory Test
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.done = True
        

    def update(self, fr):

        if self.Text_handler.is_active():
            return

        current_pos = pygame.mouse.get_pos()

        if not self.done:

            if len(self.mouse_pos) == 0:
                self.mouse_pos.append(current_pos)
                return

            prev_pos = self.mouse_pos[-1]

            movement = (
                current_pos[0] - prev_pos[0],
                current_pos[1] - prev_pos[1]
            )

            # Only compute if actual movement happened
            if movement != (0, 0):

                # Ideal direction toward box
                target = self.rect.center
                ideal_vec = (
                    target[0] - prev_pos[0],
                    target[1] - prev_pos[1]
                )

                # Normalize both
                movement_mag = math.hypot(*movement)
                ideal_mag = math.hypot(*ideal_vec)

                if movement_mag > 0 and ideal_mag > 0:
                    movement_unit = (
                        movement[0] / movement_mag,
                        movement[1] / movement_mag
                    )

                    ideal_unit = (
                        ideal_vec[0] / ideal_mag,
                        ideal_vec[1] / ideal_mag
                    )

                    # Dot product gives cos(theta)
                    dot = movement_unit[0] * ideal_unit[0] + movement_unit[1] * ideal_unit[1]

                    # Clamp for safety
                    dot = max(-1, min(1, dot))

                    angle_error = math.acos(dot)  # radians

                    self.direction_errors.append(angle_error)

            self.mouse_pos.append(current_pos)

        if self.done and not self.collected_score:
            self.collected_score = True
            self.calculate_loss()
            
        
    def draw(self, screen):
        self._render_title(screen)

        pygame.draw.rect(screen, (200, 50, 50), self.rect)

        # Draw trajectory
        if len(self.mouse_pos) > 1:
            pygame.draw.lines(
                screen,
                (100, 200, 255),
                False,
                self.mouse_pos,
                2
            )


    def _render_title(self, screen):
        if self.Text_handler.is_active():
            self.Textbox.render()
        else:
            text = self.font.render("Mouse Trajectory Test", True, (255,255,255))
            screen.blit(text, (250, 300))

    def is_done(self):
        return self.done
    
    def calculate_loss(self):

        if len(self.direction_errors) == 0:
            return

        mse = sum(e**2 for e in self.direction_errors) / len(self.direction_errors)
        rmse = math.sqrt(mse)

        print("Directional RMSE (radians):", rmse)

        score = self.get_score(rmse)
    

        self.controller.game.results.append(score)


    def get_score(self, rmse):
        score = 0

        if rmse > 0.2: #you human
            score = 0
        if rmse < 0.2: #ai
            score += 20

        return score